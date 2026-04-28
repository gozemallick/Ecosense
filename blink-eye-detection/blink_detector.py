import argparse
from pathlib import Path

import cv2


def resolve_cascade(name):
    local_path = Path(name)
    if local_path.exists():
        return str(local_path)
    return str(Path(cv2.data.haarcascades) / name)


def run_blink_detector(camera_index=0, scale_factor=1.3, min_neighbors=5):
    face_cascade = cv2.CascadeClassifier(resolve_cascade("haarcascade_frontalface_default.xml"))
    eye_cascade = cv2.CascadeClassifier(resolve_cascade("haarcascade_eye.xml"))

    if face_cascade.empty() or eye_cascade.empty():
        raise RuntimeError("Could not load Haar cascade XML files.")

    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera index {camera_index}.")

    blink_count = 0
    eyes_closed = False

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scale_factor, min_neighbors)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y : y + h, x : x + w]
                roi_color = frame[y : y + h, x : x + w]

                eyes = eye_cascade.detectMultiScale(roi_gray)
                if len(eyes) == 0:
                    if not eyes_closed:
                        blink_count += 1
                        eyes_closed = True
                else:
                    eyes_closed = False

                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            cv2.putText(
                frame,
                f"Blinks: {blink_count}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )
            cv2.imshow("Eye Blink Detection", frame)

            if cv2.waitKey(30) & 0xFF == 27:
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(description="Run webcam eye blink detection with OpenCV.")
    parser.add_argument("--camera", type=int, default=0, help="Camera index to use.")
    parser.add_argument("--scale-factor", type=float, default=1.3, help="Haar cascade scale factor.")
    parser.add_argument("--min-neighbors", type=int, default=5, help="Haar cascade min neighbors.")
    args = parser.parse_args()

    run_blink_detector(args.camera, args.scale_factor, args.min_neighbors)


if __name__ == "__main__":
    main()
