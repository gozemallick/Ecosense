import argparse
from pathlib import Path

import pandas as pd


def combine_csvs(input_dir, output_file):
    input_dir = Path(input_dir)
    output_file = Path(output_file)

    csv_files = sorted(input_dir.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {input_dir}")

    frames = [pd.read_csv(path) for path in csv_files]
    combined = pd.concat(frames, ignore_index=True)
    combined.to_csv(output_file, index=False)
    return output_file, len(csv_files), len(combined)


def main():
    parser = argparse.ArgumentParser(description="Combine monthly ecommerce sales CSV files.")
    parser.add_argument("--input-dir", default=".", help="Folder containing monthly CSV files.")
    parser.add_argument("--output", default="combined_csv_file.csv", help="Output combined CSV path.")
    args = parser.parse_args()

    output_file, file_count, row_count = combine_csvs(args.input_dir, args.output)
    print(f"Combined {file_count} files into {output_file} with {row_count:,} rows.")


if __name__ == "__main__":
    main()
