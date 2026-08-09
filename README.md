# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-09 06:30:29 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 32.1 °C |
| 💧 Humidity | 74 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 10.3 km/h |
| 🧭 Wind Direction | 113° |
| 🔵 Pressure | 978.9 hPa |
| 🌫️ AQI (US) | 99 — Moderate 🟡 |
| PM2.5 | 26.9 µg/m³ |
| PM10 | 27.2 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-09 06:30:29 | 32.1 | 0.0 | 99 | 10.3 | 74 |
| 2026-08-09 05:30:34 | 31.7 | 0.1 | 100 | 10.3 | 74 |
| 2026-08-09 04:42:12 | 30.7 | 0.0 | 101 | 10.0 | 78 |
| 2026-08-09 04:30:30 | 30.7 | 0.0 | 101 | 10.0 | 78 |
| 2026-08-09 03:30:22 | 29.5 | 0.0 | 102 | 12.1 | 84 |
| 2026-08-09 02:30:22 | 28.9 | 0.1 | 102 | 10.4 | 87 |
| 2026-08-09 01:30:26 | 28.1 | 0.0 | 102 | 8.3 | 90 |
| 2026-08-09 00:30:26 | 27.2 | 0.0 | 103 | 7.7 | 92 |
| 2026-08-08 23:30:24 | 27.0 | 0.0 | 103 | 7.0 | 92 |
| 2026-08-08 22:30:25 | 27.2 | 0.0 | 104 | 7.2 | 92 |
| 2026-08-08 21:30:24 | 27.4 | 0.0 | 104 | 8.6 | 91 |
| 2026-08-08 20:30:22 | 27.7 | 0.0 | 104 | 9.5 | 90 |
| 2026-08-08 19:30:30 | 27.9 | 0.0 | 106 | 8.6 | 89 |
| 2026-08-08 18:30:33 | 28.4 | 0.0 | 107 | 11.7 | 86 |
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

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 1 day(s)</summary>

**2026-08-08**
![2026-08-08 trend](data/chart-history/2026-08-08.png)

</details>
<!-- HISTORY-END -->

## 📁 Repo structure

```
weather-logger/
├── .github/workflows/update-weather.yml
├── data/weather_log.csv
├── data/day_chart.png
├── data/chart-history/        # rolling last 7 days, e.g. 2026-08-08.png
├── scripts/fetch_weather.py
├── scripts/update_readme.py
├── scripts/generate_chart.py
├── README.md
└── requirements.txt
```
