"""
Read data/weather_log.csv and rewrite the auto-generated section of
README.md between the DATA-START / DATA-END markers.
"""
import csv
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "weather_log.csv")
README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")

START_MARKER = "<!-- DATA-START -->"
END_MARKER = "<!-- DATA-END -->"


def aqi_category(aqi):
    try:
        aqi = float(aqi)
    except (TypeError, ValueError):
        return "Unknown"
    if aqi <= 50:
        return "Good \U0001F7E2"
    if aqi <= 100:
        return "Moderate \U0001F7E1"
    if aqi <= 150:
        return "Unhealthy for Sensitive Groups \U0001F7E0"
    if aqi <= 200:
        return "Unhealthy \U0001F534"
    if aqi <= 300:
        return "Very Unhealthy \U0001F7E3"
    return "Hazardous \u26AB"


def read_rows():
    if not os.path.isfile(CSV_PATH):
        return []
    with open(CSV_PATH, newline="") as f:
        return list(csv.DictReader(f))


def build_section(rows):
    if not rows:
        return "No data logged yet. The workflow runs hourly — check back soon."

    latest = rows[-1]
    recent = rows[-24:][::-1]  # last 24 readings, newest first

    lines = []
    lines.append(f"**Last updated:** `{latest['timestamp_utc']} UTC`\n")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| 🌡️ Temperature | {latest['temperature_c']} °C |")
    lines.append(f"| 💧 Humidity | {latest['humidity_percent']} % |")
    lines.append(f"| 🌧️ Rain (last hr) | {latest.get('rain_mm') or '0'} mm |")
    lines.append(f"| 💨 Wind Speed | {latest['wind_speed_kmh']} km/h |")
    lines.append(f"| 🧭 Wind Direction | {latest['wind_direction_deg']}° |")
    lines.append(f"| 🔵 Pressure | {latest['pressure_hpa']} hPa |")
    lines.append(f"| 🌫️ AQI (US) | {latest['aqi_us']} — {aqi_category(latest['aqi_us'])} |")
    lines.append(f"| PM2.5 | {latest['pm2_5']} µg/m³ |")
    lines.append(f"| PM10 | {latest['pm10']} µg/m³ |")
    lines.append("")
    lines.append(f"<details><summary>Last {len(recent)} readings</summary>\n")
    lines.append("| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |")
    lines.append("|---|---|---|---|---|---|")
    for r in recent:
        lines.append(
            f"| {r['timestamp_utc']} | {r['temperature_c']} | {r.get('rain_mm') or '0'} | "
            f"{r['aqi_us']} | {r['wind_speed_kmh']} | {r['humidity_percent']} |"
        )
    lines.append("\n</details>")

    return "\n".join(lines)


def update_readme():
    section = build_section(read_rows())
    if not os.path.isfile(README_PATH):
        raise FileNotFoundError("README.md not found")

    with open(README_PATH, "r") as f:
        content = f.read()

    if START_MARKER not in content or END_MARKER not in content:
        raise ValueError(f"README.md must contain {START_MARKER} and {END_MARKER} markers")

    pre = content.split(START_MARKER)[0]
    post = content.split(END_MARKER)[1]
    new_content = f"{pre}{START_MARKER}\n{section}\n{END_MARKER}{post}"

    with open(README_PATH, "w") as f:
        f.write(new_content)

    print("README.md updated.")


if __name__ == "__main__":
    update_readme()
