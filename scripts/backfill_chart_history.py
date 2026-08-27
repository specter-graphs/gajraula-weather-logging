"""
Backfill data/chart-history/ with a chart for every complete calendar day
(IST) found in data/weather_log.csv that doesn't already have one.

generate_chart.py only ever renders "yesterday" on each run, and an older
version of this project deleted anything past the most recent 7 days. The
raw CSV log was never trimmed though, so every day's data is still there -
this script just re-renders the charts that limit had deleted and drops
them back into data/chart-history/. It's safe to re-run any time: existing
PNGs are left untouched and only missing days are (re)generated.

The most recent IST calendar day in the CSV is skipped, since it's very
likely still in progress and not a complete day yet.
"""
import os
from datetime import timedelta

from generate_chart import HISTORY_DIR, IST, day_window, load_rows, render_day_chart


def main():
    rows = load_rows()
    if not rows:
        print("No data in weather_log.csv yet, nothing to backfill.")
        return

    first_date = min(ts.astimezone(IST).date() for ts, _ in rows)
    last_date = max(ts.astimezone(IST).date() for ts, _ in rows)

    os.makedirs(HISTORY_DIR, exist_ok=True)

    created, already_present, no_data = 0, 0, 0
    day_date = first_date
    while day_date < last_date:  # exclude the last (likely incomplete) day
        out_path = os.path.join(HISTORY_DIR, f"{day_date.isoformat()}.png")
        if os.path.exists(out_path):
            already_present += 1
        else:
            day_start_ist, day_end_ist, window = day_window(rows, day_date)
            if render_day_chart(day_date, day_start_ist, day_end_ist, window, out_path):
                print(f"Backfilled {out_path}")
                created += 1
            else:
                print(f"Not enough data for {day_date}, skipped.")
                no_data += 1
        day_date += timedelta(days=1)

    print(
        f"\nDone. Created {created}, already present {already_present}, "
        f"skipped (no data) {no_data}."
    )


if __name__ == "__main__":
    main()
