import argparse
from collections import Counter
from itertools import combinations

import pandas as pd


def find_top_pairs(csv_path, top_n=10):
    df = pd.read_csv(csv_path)
    df = df[df["Order ID"] != "Order ID"].dropna(subset=["Order ID", "Product"])

    multi_product_orders = df[df["Order ID"].duplicated(keep=False)].copy()
    multi_product_orders["Grouped"] = multi_product_orders.groupby("Order ID")["Product"].transform(
        lambda products: ",".join(products)
    )
    grouped = multi_product_orders[["Order ID", "Grouped"]].drop_duplicates()

    pair_counts = Counter()
    for products in grouped["Grouped"]:
        unique_products = sorted(set(products.split(",")))
        pair_counts.update(combinations(unique_products, 2))

    return pair_counts.most_common(top_n)


def main():
    parser = argparse.ArgumentParser(description="Find frequently bought-together product pairs.")
    parser.add_argument("--csv", default="combined_csv_file.csv", help="Combined ecommerce sales CSV path.")
    parser.add_argument("--top", type=int, default=10, help="Number of product pairs to show.")
    args = parser.parse_args()

    for pair, count in find_top_pairs(args.csv, args.top):
        print(f"{pair}: {count}")


if __name__ == "__main__":
    main()
