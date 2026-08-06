"""
Fetch current weather + air quality data from Open-Meteo (free, no API key)
and append one row to data/weather_log.csv.
"""
import csv
import os
import sys
from datetime import datetime, timezone

import requests

LAT = os.environ.get("WEATHER_LAT", "28.8500")
LON = os.environ.get("WEATHER_LON", "78.2333")

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "weather_log.csv")

FIELDNAMES = [
    "timestamp_utc",
    "temperature_c",
    "humidity_percent",
    "wind_speed_kmh",
    "wind_direction_deg",
    "pressure_hpa",
    "weather_code",
    "aqi_us",
    "pm2_5",
    "pm10",
    "co",
    "no2",
    "o3",
]


def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LAT,
        "longitude": LON,
        "current": (
            "temperature_2m,relative_humidity_2m,wind_speed_10m,"
            "wind_direction_10m,surface_pressure,weather_code"
        ),
        "timezone": "UTC",
    }
    r = requests.get(url, params=params, timeout=20)
    r.raise_for_status()
    return r.json().get("current", {})


def fetch_air_quality():
    url = "https://air-quality-api.open-meteo.com/v1/air-quality"
    params = {
        "latitude": LAT,
        "longitude": LON,
        "current": "us_aqi,pm2_5,pm10,carbon_monoxide,nitrogen_dioxide,ozone",
        "timezone": "UTC",
    }
    r = requests.get(url, params=params, timeout=20)
    r.raise_for_status()
    return r.json().get("current", {})


def append_row(row):
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    write_header = (not os.path.isfile(CSV_PATH)) or os.path.getsize(CSV_PATH) == 0
    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow(row)


def main():
    try:
        weather = fetch_weather()
        aq = fetch_air_quality()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)

    row = {
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "temperature_c": weather.get("temperature_2m"),
        "humidity_percent": weather.get("relative_humidity_2m"),
        "wind_speed_kmh": weather.get("wind_speed_10m"),
        "wind_direction_deg": weather.get("wind_direction_10m"),
        "pressure_hpa": weather.get("surface_pressure"),
        "weather_code": weather.get("weather_code"),
        "aqi_us": aq.get("us_aqi"),
        "pm2_5": aq.get("pm2_5"),
        "pm10": aq.get("pm10"),
        "co": aq.get("carbon_monoxide"),
        "no2": aq.get("nitrogen_dioxide"),
        "o3": aq.get("ozone"),
    }
    append_row(row)
    print(f"Logged: {row}")


if __name__ == "__main__":
    main()
