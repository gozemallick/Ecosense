# Eye Blink Detection

This project detects eye blinks from a live webcam feed using OpenCV.

## Overview

The notebook uses Haar cascade classifiers to detect:

- Face region.
- Eye region inside the detected face.

When the face is visible but eyes are not detected for a short moment, the system counts it as a blink.

## Pipeline

```text
Webcam video stream
        |
        v
Read frame using OpenCV
        |
        v
Convert frame to grayscale
        |
        v
Detect face with Haar cascade
        |
        v
Detect eyes inside face ROI
        |
        v
If eyes disappear, count blink
        |
        v
Display annotated webcam frame
```

## Main File

```text
eye_blink_detection.ipynb
```

Runnable script:

```text
blink_detector.py
```

## Dependencies

Install dependencies from the root repository:

```bash
pip install -r ../requirements.txt
```

## Required Haar Cascades

The notebook expects these files:

```text
haarcascade_frontalface_default.xml
haarcascade_eye.xml
```

They can be downloaded from the OpenCV Haar cascade repository or loaded from OpenCV's installed data folder.

## How to Run

Open the notebook:

```bash
jupyter notebook eye_blink_detection.ipynb
```

Run the webcam detection cell. Press `Esc` to stop the camera window.

Or run the script directly:

```bash
python blink_detector.py
```

Optional camera selection:

```bash
python blink_detector.py --camera 0
```

## Current Logic

The core blink detection idea is:

```python
if len(eyes) == 0:
    if not prev_eye_state:
        blink_count += 1
        prev_eye_state = True
else:
    prev_eye_state = False
```

This avoids counting the same closed-eye moment many times in continuous frames.

## Suggested Improvements

- Use OpenCV's built-in cascade path instead of requiring XML files in the folder.
- Add an eye aspect ratio method using facial landmarks for better accuracy.
- Add blink rate per minute.
- Add CSV logging for timestamp and blink count.
- Add a small demo screenshot or GIF.
- Convert the notebook into a Python script such as `blink_detector.py`.
- Add a small evaluation dataset instead of manually estimated blink labels.

## Limitations

Haar cascade eye detection is sensitive to lighting, camera angle, glasses, and face movement. For a more robust system, use MediaPipe Face Mesh or dlib facial landmarks.
