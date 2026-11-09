"""Generate a deliberately messy dataset for the data-cleaning class."""

import csv
import random
from pathlib import Path


def main():
    rng = random.Random(42)
    row_count = 1600

    # There are only 1,000 four-digit IDs beginning with 1, so some repeat.
    participant_ids = list(range(1000, 2000)) + list(range(1000, 1593))
    rng.shuffle(participant_ids)
    participant_ids = list(range(9000, 9007)) + participant_ids

    gender_values = ("male", "female", "m", "f", "M", "F")
    genders = [gender_values[i % len(gender_values)] for i in range(row_count - 1)]
    genders.append("male ")
    rng.shuffle(genders)

    country_values = ("Norway", "UK", "England", "USA", "Finland", "Sweden", "Poland")
    cohort_values = ("first", "second", "third")
    countries = [rng.choice(country_values) for _ in range(row_count)]
    cohorts = [rng.choice(cohort_values) for _ in range(row_count)]
    conditions = ["caf", "dcaf"] * (row_count // 2)
    rng.shuffle(conditions)
    juggling_times = [
        rng.randint(60, 180) if condition == "caf" else rng.randint(0, 120)
        for condition in conditions
    ]
    country_effects = {
        "Norway": 0.7,
        "UK": 0.2,
        "England": 0.3,
        "USA": -0.3,
        "Finland": 2.5,
        "Sweden": 0.0,
        "Poland": -0.7,
    }
    max_pineapples = [
        max(
            1,
            min(
                10 if country == "Finland" else 6,
                round(
                    3.5 + country_effects[country] + (time - 90) / 150
                    + rng.gauss(0, 1.5 if country == "Finland" else 1.2)
                ),
            ),
        )
        for country, time in zip(countries, juggling_times)
    ]

    output_path = Path(__file__).resolve().parent.parent / "data" / "dummy_experiment.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file, delimiter=";")
        writer.writerow(
            ["Participant ID", "Gender", "Country of Origin", "Cohort", "Condition", "Juggling time", "Max pineapples"]
        )
        for participant_id, gender, country, cohort, condition, time, pineapples in zip(
            participant_ids, genders, countries, cohorts, conditions,
            juggling_times, max_pineapples,
        ):
            if str(participant_id).startswith("9"):
                writer.writerow([participant_id, "", "", "", "", "", ""])
            else:
                writer.writerow(
                    [participant_id, gender, country, cohort, condition, f"{time} seconds", pineapples]
                )

    print(f"Wrote {row_count} rows to {output_path}")


if __name__ == "__main__":
    main()
