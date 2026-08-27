"""
Generate a full previous-day trend chart from data/weather_log.csv, and
keep every one of them in data/chart-history/ (no retention limit - the
history grows forever, one PNG per calendar day).

Always plots "yesterday" - the last fully completed calendar day in
IST (00:00-23:59) - rather than a rolling last-24h window. That means
the chart is identical across every hourly run within the same day,
and only actually changes once every 24h when a new day rolls over,
so the committed PNGs don't churn the repo's git history every hour.

Each day's chart is saved as data/chart-history/YYYY-MM-DD.png, and the
same image is copied to data/day_chart.png (a stable "latest" filename
for the main README section to embed).

To backfill charts for older days already in the CSV (e.g. to restore
ones an earlier, day-limited version of this script deleted), run
scripts/backfill_chart_history.py.

Every logged metric is min-max normalized to a 0-100 scale so wildly
different units (C, %, ug/m3, hPa...) can be compared by shape on one
chart. Actual value ranges are kept in the legend labels.
"""
import csv
import os
import shutil
from datetime import datetime, timedelta, timezone

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "weather_log.csv")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "day_chart.png")
HISTORY_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "chart-history")

IST = timezone(timedelta(hours=5, minutes=30))

# field -> (label, unit, color, is_hero)
# "hero" metrics (temperature + AQI) are drawn bold and opaque; the rest
# are drawn thinner/lighter so the chart stays readable with ~10 lines.
FIELDS = {
    "temperature_c":    ("Temperature", "\u00b0C",  "#E4572E", True),
    "aqi_us":           ("AQI (US)",    "",         "#C4302B", True),
    "humidity_percent": ("Humidity",    "%",        "#3A8DDE", False),
    "pm2_5":            ("PM2.5",       "\u00b5g/m\u00b3", "#A9744F", False),
    "pm10":             ("PM10",        "\u00b5g/m\u00b3", "#C9A66B", False),
    "wind_speed_kmh":   ("Wind Speed",  "km/h",     "#3F9C6D", False),
    "pressure_hpa":     ("Pressure",    "hPa",      "#4A5A7A", False),
    "co":               ("CO",          "\u00b5g/m\u00b3", "#7C8794", False),
    "no2":              ("NO\u2082",    "\u00b5g/m\u00b3", "#C2477A", False),
    "o3":               ("O\u2083",     "\u00b5g/m\u00b3", "#7B5EA7", False),
    "rain_mm":          ("Rain",        "mm",       "#4FC3D9", False),
}


def to_float(v):
    try:
        if v is None or v == "":
            return None
        return float(v)
    except ValueError:
        return None


def load_rows():
    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        rows = []
        for r in reader:
            try:
                ts = datetime.strptime(
                    r["timestamp_utc"], "%Y-%m-%d %H:%M:%S"
                ).replace(tzinfo=timezone.utc)
            except (ValueError, KeyError, TypeError):
                continue
            rows.append((ts, r))
        return rows


def day_window(rows, day_date):
    """Return (day_start_ist, day_end_ist, window) for a given IST calendar date.

    window is the subset of (timestamp, row) pairs falling in that day,
    sorted chronologically.
    """
    day_start_ist = datetime.combine(day_date, datetime.min.time(), tzinfo=IST)
    day_end_ist = day_start_ist + timedelta(days=1)
    window = sorted(
        (pair for pair in rows if day_start_ist <= pair[0].astimezone(IST) < day_end_ist),
        key=lambda p: p[0],
    )
    return day_start_ist, day_end_ist, window


def render_day_chart(day_date, day_start_ist, day_end_ist, window, out_path):
    """Render the normalized multi-metric trend chart for one day to out_path.

    Returns True if a chart was drawn, False if there wasn't enough data.
    """
    if len(window) < 2:
        return False

    times_ist = [ts.astimezone(IST) for ts, _ in window]

    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=140)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    plotted_any = False
    for field, (label, unit, color, is_hero) in FIELDS.items():
        values = [to_float(r.get(field)) for _, r in window]
        present = [v for v in values if v is not None]
        if len(present) < 2:
            continue
        vmin, vmax = min(present), max(present)
        if vmax == vmin:
            continue  # flat/no variation in this window, not worth a line

        norm = [
            ((v - vmin) / (vmax - vmin) * 100) if v is not None else float("nan")
            for v in values
        ]
        unit_str = f" {unit}" if unit else ""
        legend_label = f"{label} ({vmin:g}\u2013{vmax:g}{unit_str})"

        ax.plot(
            times_ist,
            norm,
            label=legend_label,
            color=color,
            linewidth=2.8 if is_hero else 1.4,
            alpha=1.0 if is_hero else 0.6,
            solid_capstyle="round",
        )
        plotted_any = True

    if not plotted_any:
        plt.close(fig)
        return False

    ax.set_ylabel("Relative to each metric's own daily range (%)", fontsize=10, color="#555")
    ax.set_ylim(-5, 105)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.tick_params(axis="y", labelsize=9, colors="#555")

    ax.set_xlim(day_start_ist, day_end_ist)
    ax.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0, 24, 2), tz=IST))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M", tz=IST))
    ax.tick_params(axis="x", labelsize=9, colors="#555")

    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#ccc")
    ax.grid(axis="y", color="#e9e9e9", linewidth=0.8)
    ax.set_axisbelow(True)

    ax.set_title(
        f"Gajraula \u2014 Full-Day Trend \u2014 {day_start_ist.strftime('%A, %b %d %Y')}",
        fontsize=15, fontweight="bold", color="#222", pad=14, loc="left",
    )

    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=3,
        fontsize=9.2,
        frameon=False,
        labelcolor="#333",
    )

    fig.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fig.savefig(out_path, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return True


def main():
    rows = load_rows()
    if not rows:
        print("No data yet, skipping chart.")
        return

    latest_utc = max(ts for ts, _ in rows)
    yesterday_ist_date = latest_utc.astimezone(IST).date() - timedelta(days=1)
    day_start_ist, day_end_ist, window = day_window(rows, yesterday_ist_date)

    dated_path = os.path.join(HISTORY_DIR, f"{yesterday_ist_date.isoformat()}.png")
    ok = render_day_chart(yesterday_ist_date, day_start_ist, day_end_ist, window, dated_path)
    if not ok:
        print(f"No data logged for {yesterday_ist_date}, skipping chart.")
        return

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    shutil.copyfile(dated_path, OUT_PATH)
    print(f"Chart saved to {dated_path} (and copied to {OUT_PATH})")


if __name__ == "__main__":
    main()
