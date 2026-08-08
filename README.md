# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-08 17:30:22 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 28.7 °C |
| 💧 Humidity | 85 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 11.9 km/h |
| 🧭 Wind Direction | 96° |
| 🔵 Pressure | 979.0 hPa |
| 🌫️ AQI (US) | 108 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 32.9 µg/m³ |
| PM10 | 33.2 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-08 17:30:22 | 28.7 | 0.0 | 108 | 11.9 | 85 |
| 2026-08-08 16:30:23 | 28.9 | 0.0 | 109 | 11.9 | 85 |
| 2026-08-08 15:30:23 | 29.0 | 0.0 | 128 | 9.6 | 85 |
| 2026-08-08 14:30:28 | 29.1 | 0.0 | 142 | 5.3 | 85 |
| 2026-08-08 13:30:24 | 29.8 | 0.0 | 148 | 7.1 | 83 |
| 2026-08-08 12:30:25 | 31.2 | 0.0 | 144 | 8.0 | 76 |
| 2026-08-08 11:30:23 | 31.3 | 0.0 | 133 | 6.5 | 75 |
| 2026-08-08 10:30:28 | 31.5 | 0.0 | 118 | 9.6 | 74 |
| 2026-08-08 09:30:24 | 31.7 | 0.0 | 99 | 10.8 | 74 |
| 2026-08-08 08:30:22 | 31.0 | 0.0 | 99 | 13.4 | 79 |
| 2026-08-08 07:30:22 | 31.1 | 0.1 | 98 | 15.1 | 78 |
| 2026-08-08 06:30:23 | 31.4 | 0.0 | 97 | 18.0 | 75 |
| 2026-08-08 05:30:31 | 30.6 | 0.0 | 96 | 17.4 | 77 |
| 2026-08-08 04:30:28 | 29.6 | 0.0 | 95 | 17.2 | 80 |
| 2026-08-08 03:30:28 | 28.5 | 0.0 | 94 | 16.2 | 85 |
| 2026-08-08 02:30:25 | 27.7 | 0.0 | 93 | 14.6 | 89 |
| 2026-08-08 01:30:25 | 26.8 | 0.0 | 92 | 15.0 | 92 |
| 2026-08-08 00:30:22 | 25.8 | 0.0 | 90 | 13.1 | 93 |
| 2026-08-07 23:30:27 | 26.6 | 0.0 | 90 | 10.6 | 95 |
| 2026-08-07 22:30:31 | 26.8 | 0.0 | 90 | 10.9 | 95 |
| 2026-08-07 21:30:23 | 26.8 | 0.0 | 88 | 11.5 | 95 |
| 2026-08-07 20:30:31 | 26.8 | 0.0 | 89 | 12.5 | 95 |
| 2026-08-07 19:30:25 | 26.8 | 0.0 | 91 | 12.6 | 95 |
| 2026-08-07 18:30:32 | 26.6 | 0.0 | 92 | 10.2 | 96 |

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
