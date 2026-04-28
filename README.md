# EcoSense - Ecommerce Market Basket Analysis

This public repository contains an ecommerce sales analysis and market basket analysis project.

The project studies sales transactions, product performance, customer purchase timing, city-wise demand, and frequently bought-together products. The goal is to turn raw ecommerce order data into useful business insights for marketing, inventory planning, and product bundling.

## Repository Structure

```text
Ecosense/
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

## Main Project

Open the project folder:

```text
ecommerce-market-basket-analysis/
```

Main notebook:

```text
ecommerce-market-basket-analysis/ecommerce_market_basket_analysis.ipynb
```

## What This Project Does

- Combines monthly ecommerce sales CSV files.
- Cleans repeated header rows and missing values.
- Converts quantity, price, and date columns into usable data types.
- Creates useful features such as month, hour, city, sales, and product category.
- Analyzes total orders, total products sold, and total sales.
- Finds best-performing cities, months, hours, products, and categories.
- Performs market basket analysis to find products frequently bought together.
- Estimates product purchase probabilities.

## Data Pipeline

```text
Monthly sales CSV files
        |
        v
Combine into combined_csv_file.csv
        |
        v
Clean rows and convert data types
        |
        v
Create time, city, category, and sales features
        |
        v
Sales trend and product analysis
        |
        v
Market basket pair analysis
        |
        v
Business recommendations
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Combine monthly CSV files:

```bash
python ecommerce-market-basket-analysis/combine_sales_csvs.py --input-dir path/to/monthly_csvs --output ecommerce-market-basket-analysis/combined_csv_file.csv
```

Find top product pairs:

```bash
python ecommerce-market-basket-analysis/market_basket_pairs.py --csv ecommerce-market-basket-analysis/combined_csv_file.csv --top 10
```

Run the full notebook:

```bash
jupyter notebook ecommerce-market-basket-analysis/ecommerce_market_basket_analysis.ipynb
```

## Notes

The dataset CSV is not included in this repository. Add `combined_csv_file.csv` locally or generate it from monthly sales CSV files before running the notebook.

The separate eye blink detection project should live in its own repository, because it is a computer vision project and not related to ecommerce analytics.
