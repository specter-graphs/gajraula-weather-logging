# 🌦️ Weather & AQI Logger

Automated weather station — temperature, humidity, wind, pressure, and air quality (AQI), fetched **every hour** via GitHub Actions and logged straight into this repo.

- **Data source:** [Open-Meteo](https://open-meteo.com/) (free, no API key required)
- **Update frequency:** every hour, via `.github/workflows/update-weather.yml`
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-07 01:52:21 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 26.7 °C |
| 💧 Humidity | 92 % |
| 💨 Wind Speed | 13.2 km/h |
| 🧭 Wind Direction | 70° |
| 🔵 Pressure | 975.8 hPa |
| 🌫️ AQI (US) | 92 — Moderate 🟡 |
| PM2.5 | 36.1 µg/m³ |
| PM10 | 36.2 µg/m³ |

<details><summary>Last 2 readings</summary>

| Time (UTC) | Temp °C | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|
| 2026-08-07 01:52:21 | 26.7 | 92 | 13.2 | 92 |
| 2026-08-07 00:32:38 | 26.0 | 90 | 11.1 | 95 |

</details>
<!-- DATA-END -->


## 📁 Repo structure

```
weather-logger/
├── .github/workflows/update-weather.yml
├── data/weather_log.csv
├── scripts/fetch_weather.py
├── scripts/update_readme.py
├── README.md
└── requirements.txt
```
