# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-08 01:30:25 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 26.8 °C |
| 💧 Humidity | 92 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 15.0 km/h |
| 🧭 Wind Direction | 110° |
| 🔵 Pressure | 977.1 hPa |
| 🌫️ AQI (US) | 92 — Moderate 🟡 |
| PM2.5 | 41.3 µg/m³ |
| PM10 | 41.6 µg/m³ |

<details><summary>Last 19 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-08 01:30:25 | 26.8 | 0.0 | 92 | 15.0 | 92 |
| 2026-08-08 00:30:22 | 25.8 | 0.0 | 90 | 13.1 | 93 |
| 2026-08-07 23:30:27 | 26.6 | 0.0 | 90 | 10.6 | 95 |
| 2026-08-07 22:30:31 | 26.8 | 0.0 | 90 | 10.9 | 95 |
| 2026-08-07 21:30:23 | 26.8 | 0.0 | 88 | 11.5 | 95 |
| 2026-08-07 20:30:31 | 26.8 | 0.0 | 89 | 12.5 | 95 |
| 2026-08-07 19:30:25 | 26.8 | 0.0 | 91 | 12.6 | 95 |
| 2026-08-07 18:30:32 | 26.6 | 0.0 | 92 | 10.2 | 96 |
| 2026-08-07 17:30:25 | 26.6 | 0.2 | 94 | 9.0 | 96 |
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
