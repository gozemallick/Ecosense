# Ecommerce Market Basket Analysis

This project analyzes ecommerce sales data to understand sales trends, customer purchase timing, product performance, and frequently bought-together products.

## Overview

The notebook performs exploratory data analysis and market basket analysis on ecommerce order data. It creates useful business insights such as:

- Which city generated the most orders.
- Which month had the highest sales.
- Which hour is best for advertising.
- Which products and categories sold the most.
- Which product pairs are frequently bought together.
- Product purchase probability by month.

## Main File

```text
ecommerce_market_basket_analysis.ipynb
```

Helper scripts:

| File | Purpose |
| --- | --- |
| `combine_sales_csvs.py` | Combines monthly sales CSV files into one `combined_csv_file.csv`. |
| `market_basket_pairs.py` | Finds the most frequent product pairs from a combined sales CSV. |

## Input Data

The notebook expects a combined ecommerce CSV file:

```text
combined_csv_file.csv
```

The original notebook also includes commented logic for combining monthly CSV files such as:

```text
Sales_January.csv
Sales_February.csv
Sales_March.csv
...
Sales_December.csv
```

If you have monthly CSV files, combine them first and save the final file as `combined_csv_file.csv`.

You can use the helper script:

```bash
python combine_sales_csvs.py --input-dir path/to/monthly_csvs --output combined_csv_file.csv
```

## Data Pipeline

```text
Monthly sales CSV files
        |
        v
Combine into one CSV
        |
        v
Load combined_csv_file.csv
        |
        v
Remove repeated header rows
        |
        v
Drop missing values
        |
        v
Convert data types
        |
        v
Create date, city, and sales features
        |
        v
Perform sales and product analysis
        |
        v
Market basket analysis
```

## Feature Engineering

The notebook creates:

- `Year`
- `Month`
- `Hour`
- `Minute`
- `Sales = Quantity Ordered * Price Each`
- `Cities` from purchase address
- `Category` from product name

## Analysis Performed

### Sales Analysis

- Total orders.
- Total products sold.
- Total yearly sales.
- Orders by city.
- Orders by month.
- Monthly sales.
- Sales by hour.

### Product Analysis

- Product quantity ordered.
- Product category distribution.
- Product category sales.
- Product purchase probability.
- Monthly purchase probability for selected products.

### Market Basket Analysis

The notebook groups products by `Order ID`, then counts product pairs bought together:

```python
data = df[df["Order ID"].duplicated(keep=False)]
data["Grouped"] = df.groupby("Order ID")["Product"].transform(lambda x: ",".join(x))
```

Then it uses combinations to find common pairs:

```python
count.update(Counter(combinations(row_list, 2)))
```

This helps identify product bundling and cross-selling opportunities.

## Business Use Cases

- Recommend bundles based on frequently bought-together products.
- Schedule ads during high-order hours.
- Focus inventory planning on high-demand products and months.
- Understand city-wise demand.
- Compare category-level sales performance.

## Dependencies

Install dependencies from the root repository:

```bash
pip install -r ../requirements.txt
```

## How to Run

Open the notebook:

```bash
jupyter notebook ecommerce_market_basket_analysis.ipynb
```

Make sure `combined_csv_file.csv` is available in the same folder or update the notebook path:

```python
df = pd.read_csv("combined_csv_file.csv")
```

To quickly find product pairs without running the full notebook:

```bash
python market_basket_pairs.py --csv combined_csv_file.csv --top 10
```

## Suggested Improvements

- Add a dataset download/source section.
- Save final charts into an `assets/` folder.
- Add a summary of top findings at the start of the notebook.
- Use `mlxtend` Apriori or FP-Growth for stronger association rule mining.
- Add support, confidence, and lift metrics for product pairs.
- Create an interactive dashboard using Streamlit or Power BI.
- Refactor repeated probability code into reusable functions.

## Limitations

The current market basket section counts product pairs but does not yet calculate association rule metrics such as confidence and lift. Adding those metrics would make the recommendations stronger and more business-ready.
