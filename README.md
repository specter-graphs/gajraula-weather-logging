# 🌦️ Weather & AQI Logger

Automated weather station — temperature, humidity, wind, pressure, and air quality (AQI), fetched **every hour** via GitHub Actions and logged straight into this repo.

- **Data source:** [Open-Meteo](https://open-meteo.com/) (free, no API key required)
- **Update frequency:** every hour, via `.github/workflows/update-weather.yml`
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-07 06:13:48 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 30.6 °C |
| 💧 Humidity | 77 % |
| 💨 Wind Speed | 12.8 km/h |
| 🧭 Wind Direction | 90° |
| 🔵 Pressure | 976.6 hPa |
| 🌫️ AQI (US) | 96 — Moderate 🟡 |
| PM2.5 | 25.7 µg/m³ |
| PM10 | 25.7 µg/m³ |

<details><summary>Last 3 readings</summary>

| Time (UTC) | Temp °C | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|
| 2026-08-07 06:13:48 | 30.6 | 96 | 12.8 | 77 |
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
