# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-07 16:34:35 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 26.7 °C |
| 💧 Humidity | 96 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 8.1 km/h |
| 🧭 Wind Direction | 89° |
| 🔵 Pressure | 977.1 hPa |
| 🌫️ AQI (US) | 95 — Moderate 🟡 |
| PM2.5 | 39.1 µg/m³ |
| PM10 | 39.2 µg/m³ |

<details><summary>Last 10 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-07 16:34:35 | 26.7 | 0.0 | 95 | 8.1 | 96 |
| 2026-08-07 16:11:46 | 26.7 | 0.1 | 95 | 7.3 | 96 |
| 2026-08-07 15:42:38 | 26.8 | 0.1 | 95 | 7.3 | 96 |
| 2026-08-07 15:30:26 | 26.8 | 0 | 95 | 7.3 | 96 |
| 2026-08-07 12:30:56 | 27.5 | 0 | 94 | 11.0 | 92 |
| 2026-08-07 11:49:23 | 28.7 | 0 | 94 | 6.5 | 83 |
| 2026-08-07 09:22:20 | 31.8 | 0 | 98 | 11.3 | 74 |
| 2026-08-07 06:13:48 | 30.6 | 0 | 96 | 12.8 | 77 |
| 2026-08-07 01:52:21 | 26.7 | 0 | 92 | 13.2 | 92 |
| 2026-08-07 00:32:38 | 26.0 | 0 | 90 | 11.1 | 95 |

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
