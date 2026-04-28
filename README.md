# EcoSense Projects

This repository contains two independent projects:

1. **Eye Blink Detection** - a computer vision project that detects face/eyes from webcam video and counts blink events.
2. **Ecommerce Market Basket Analysis** - a data analysis project that studies ecommerce sales patterns, product performance, customer purchase timing, and frequently purchased product combinations.

The projects are separated into their own folders so each one has a clear purpose, setup, and workflow.

## Repository Structure

```text
Ecosense/
|-- blink-eye-detection/
|   |-- eye_blink_detection.ipynb
|   |-- blink_detector.py
|   |-- README.md
|
|-- ecommerce-market-basket-analysis/
|   |-- ecommerce_market_basket_analysis.ipynb
|   |-- combine_sales_csvs.py
|   |-- market_basket_pairs.py
|   |-- README.md
|
|-- requirements.txt
|-- .gitignore
|-- README.md
```

## Project 1: Eye Blink Detection

This project uses OpenCV Haar cascade classifiers to detect a face and eyes through a webcam feed. A blink is counted when the system detects a face but temporarily does not detect eyes.

Main ideas:

- Capture webcam frames with OpenCV.
- Convert each frame to grayscale.
- Detect face region using Haar cascade.
- Detect eyes inside the face region.
- Count blink events when eyes disappear and then reappear.

Open project:

```text
blink-eye-detection/eye_blink_detection.ipynb
```

Run as a script:

```bash
python blink-eye-detection/blink_detector.py
```

## Project 2: Ecommerce Market Basket Analysis

This project analyzes ecommerce sales data from monthly CSV files. It cleans the dataset, creates time/city/sales features, studies product and category performance, and identifies products commonly bought together.

Main ideas:

- Combine monthly sales files into one dataset.
- Clean missing values and repeated header rows.
- Create features such as month, hour, city, sales, and product category.
- Analyze best-performing months, cities, products, and categories.
- Perform market basket analysis using products purchased under the same order ID.

Open project:

```text
ecommerce-market-basket-analysis/ecommerce_market_basket_analysis.ipynb
```

Combine monthly CSV files:

```bash
python ecommerce-market-basket-analysis/combine_sales_csvs.py --input-dir path/to/monthly_csvs --output ecommerce-market-basket-analysis/combined_csv_file.csv
```

Find top product pairs:

```bash
python ecommerce-market-basket-analysis/market_basket_pairs.py --csv ecommerce-market-basket-analysis/combined_csv_file.csv
```

## Installation

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

For the blink detection project, OpenCV needs Haar cascade XML files. They are available from the OpenCV repository:

- `haarcascade_frontalface_default.xml`
- `haarcascade_eye.xml`

You can also load them from OpenCV's built-in cascade path in future code improvements.

## Recommended Next Improvements

- Add sample output screenshots for both projects.
- Add markdown explanations inside each notebook before major sections.
- Add the ecommerce dataset source or instructions for creating `combined_csv_file.csv`.
- Convert the blink detection notebook into a runnable Python script.
- Convert repeated ecommerce analysis code into helper functions.
- Add a short project report with key ecommerce insights and market basket recommendations.

## Notes

The two projects solve different problems, so they are intentionally separated. This makes the repository easier to understand for recruiters, teachers, and other developers.
