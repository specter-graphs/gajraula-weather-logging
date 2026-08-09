# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-09 14:30:32 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 29.9 °C |
| 💧 Humidity | 82 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 6.4 km/h |
| 🧭 Wind Direction | 98° |
| 🔵 Pressure | 976.6 hPa |
| 🌫️ AQI (US) | 151 — Unhealthy 🔴 |
| PM2.5 | 37.7 µg/m³ |
| PM10 | 37.8 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-09 14:30:32 | 29.9 | 0.0 | 151 | 6.4 | 82 |
| 2026-08-09 13:30:34 | 30.6 | 0.0 | 154 | 5.6 | 80 |
| 2026-08-09 12:30:30 | 31.9 | 0.0 | 149 | 5.7 | 73 |
| 2026-08-09 11:30:31 | 32.6 | 0.0 | 135 | 5.2 | 68 |
| 2026-08-09 10:30:32 | 32.9 | 0.0 | 116 | 3.8 | 68 |
| 2026-08-09 09:30:31 | 32.8 | 0.0 | 96 | 4.7 | 68 |
| 2026-08-09 08:30:30 | 32.7 | 0.1 | 97 | 5.6 | 69 |
| 2026-08-09 07:30:28 | 32.0 | 0.0 | 98 | 8.4 | 72 |
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
