
"""
Vayu Astra - Raspberry Pi Camera Preview

Reference implementation using:
- Raspberry Pi Camera Module 3
- Picamera2
- OpenCV
- Flask

SAFETY:
No motor commands are sent by this program.
"""

import time
import threading

import cv2
from flask import Flask, Response
from picamera2 import Picamera2


FRAME_WIDTH = 640
FRAME_HEIGHT = 480
JPEG_QUALITY = 80

app = Flask(__name__)

frame_lock = threading.Lock()
latest_frame = None


def camera_worker():
    global latest_frame

    camera = Picamera2()

    config = camera.create_video_configuration(
        main={
            "size": (FRAME_WIDTH, FRAME_HEIGHT),
            "format": "RGB888",
        }
    )

    camera.configure(config)
    camera.start()

    try:
        while True:
            frame = camera.capture_array()

            height, width = frame.shape[:2]
            center_x = width // 2
            center_y = height // 2

            cv2.line(
                frame,
                (center_x - 20, center_y),
                (center_x + 20, center_y),
                (0, 255, 0),
                2,
            )

            cv2.line(
                frame,
                (center_x, center_y - 20),
                (center_x, center_y + 20),
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                "VAYU ASTRA | CAMERA PREVIEW",
                (15, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2,
            )

            success, encoded = cv2.imencode(
                ".jpg",
                frame,
                [
                    cv2.IMWRITE_JPEG_QUALITY,
                    JPEG_QUALITY,
                ],
            )

            if success:
                with frame_lock:
                    latest_frame = encoded.tobytes()

            time.sleep(0.03)

    finally:
        camera.stop()


def generate_stream():
    while True:
        with frame_lock:
            frame = latest_frame

        if frame is None:
            time.sleep(0.05)
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame
            + b"\r\n"
        )

        time.sleep(0.03)


@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vayu Astra Camera</title>
        <style>
            body {
                background: #111;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 30px;
            }
            img {
                width: 90%;
                max-width: 960px;
                border: 1px solid #444;
            }
        </style>
    </head>
    <body>
        <h2>VAYU ASTRA</h2>
        <p>Raspberry Pi Camera Preview</p>
        <img src="/video_feed">
        <p>Servo control disabled in this version.</p>
    </body>
    </html>
    """


@app.route("/video_feed")
def video_feed():
    return Response(
        generate_stream(),
        mimetype=(
            "multipart/x-mixed-replace; "
            "boundary=frame"
        ),
    )


if __name__ == "__main__":
    worker = threading.Thread(
        target=camera_worker,
        daemon=True,
    )
    worker.start()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        threaded=True,
    )
