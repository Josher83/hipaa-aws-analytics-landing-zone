import argparse
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {
    "patient_id",
    "first_name",
    "last_name",
    "dob",
    "ssn",
    "diagnosis",
    "admit_date",
    "discharge_date",
}


def build_tableau_ready_views(input_path: Path, output_dir: Path) -> None:
    df = pd.read_csv(input_path)

    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        missing_columns = ", ".join(sorted(missing))
        raise ValueError(f"Missing required columns: {missing_columns}")

    for column in ["dob", "admit_date", "discharge_date"]:
        df[column] = pd.to_datetime(df[column], errors="raise")

    df["length_of_stay_days"] = (df["discharge_date"] - df["admit_date"]).dt.days
    if (df["length_of_stay_days"] < 0).any():
        raise ValueError("discharge_date cannot be earlier than admit_date")

    df["age_at_admit"] = ((df["admit_date"] - df["dob"]).dt.days / 365.25).astype(int)
    df["admit_month"] = df["admit_date"].dt.to_period("M").astype(str)
    df["patient_key"] = "P" + df["patient_id"].astype(int).astype(str).str.zfill(5)

    clean_patients = df[
        [
            "patient_key",
            "diagnosis",
            "admit_date",
            "discharge_date",
            "admit_month",
            "length_of_stay_days",
            "age_at_admit",
        ]
    ].rename(columns={"diagnosis": "diagnosis_group"})

    diagnosis_summary = (
        clean_patients.groupby(["diagnosis_group", "admit_month"], as_index=False)
        .agg(
            patient_count=("patient_key", "count"),
            avg_length_of_stay_days=("length_of_stay_days", "mean"),
        )
        .sort_values(["admit_month", "diagnosis_group"])
    )
    diagnosis_summary["avg_length_of_stay_days"] = diagnosis_summary[
        "avg_length_of_stay_days"
    ].round(2)

    output_dir.mkdir(parents=True, exist_ok=True)
    clean_patients.to_csv(output_dir / "patients_clean.csv", index=False, date_format="%Y-%m-%d")
    diagnosis_summary.to_csv(output_dir / "diagnosis_summary.csv", index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transform raw patient data into Tableau-ready CSV outputs."
    )
    parser.add_argument(
        "--input",
        default="data/raw/patients.csv",
        help="Path to raw source CSV (default: data/raw/patients.csv)",
    )
    parser.add_argument(
        "--output-dir",
        default="data/clean",
        help="Directory for transformed CSV outputs (default: data/clean)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_tableau_ready_views(Path(args.input), Path(args.output_dir))
    print(f"Wrote cleaned outputs to {args.output_dir}")


if __name__ == "__main__":
    main()
