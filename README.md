# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-16 16:30:32 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 26.5 °C |
| 💧 Humidity | 97 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 7.2 km/h |
| 🧭 Wind Direction | 158° |
| 🔵 Pressure | 978.4 hPa |
| 🌫️ AQI (US) | 137 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 35.6 µg/m³ |
| PM10 | 43.8 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-16 16:30:32 | 26.5 | 0.0 | 137 | 7.2 | 97 |
| 2026-08-16 15:30:30 | 26.8 | 0.0 | 138 | 5.5 | 98 |
| 2026-08-16 14:30:31 | 27.0 | 0.0 | 139 | 4.4 | 97 |
| 2026-08-16 13:30:33 | 27.4 | 0.1 | 139 | 3.3 | 95 |
| 2026-08-16 12:30:33 | 30.0 | 0.0 | 139 | 1.8 | 83 |
| 2026-08-16 11:30:29 | 30.1 | 0.1 | 139 | 4.7 | 82 |
| 2026-08-16 10:30:31 | 30.5 | 0.2 | 138 | 9.2 | 78 |
| 2026-08-16 09:30:34 | 32.2 | 0.0 | 109 | 8.4 | 72 |
| 2026-08-16 08:30:33 | 33.1 | 0.0 | 109 | 6.7 | 71 |
| 2026-08-16 07:30:33 | 32.1 | 0.0 | 109 | 5.9 | 75 |
| 2026-08-16 06:30:30 | 31.6 | 0.0 | 109 | 3.0 | 76 |
| 2026-08-16 05:30:30 | 30.0 | 0.0 | 109 | 4.0 | 81 |
| 2026-08-16 04:30:28 | 29.5 | 0.2 | 109 | 6.9 | 82 |
| 2026-08-16 03:30:31 | 29.7 | 0.0 | 109 | 7.0 | 83 |
| 2026-08-16 02:30:28 | 28.8 | 0.0 | 110 | 5.2 | 89 |
| 2026-08-16 01:30:31 | 27.7 | 0.0 | 112 | 5.0 | 94 |
| 2026-08-16 00:30:32 | 26.0 | 0.0 | 114 | 3.2 | 97 |
| 2026-08-15 23:30:32 | 26.0 | 0.0 | 115 | 4.6 | 98 |
| 2026-08-15 22:30:32 | 26.4 | 0.0 | 119 | 3.3 | 97 |
| 2026-08-15 21:30:32 | 26.6 | 0.1 | 121 | 1.1 | 95 |
| 2026-08-15 20:30:31 | 27.0 | 0.0 | 120 | 6.4 | 91 |
| 2026-08-15 19:30:32 | 26.3 | 0.0 | 118 | 5.2 | 99 |
| 2026-08-15 18:30:35 | 27.5 | 0.1 | 116 | 5.5 | 93 |
| 2026-08-15 17:30:35 | 28.3 | 0.0 | 114 | 3.0 | 92 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 7 day(s)</summary>

**2026-08-15**
![2026-08-15 trend](data/chart-history/2026-08-15.png)

**2026-08-14**
![2026-08-14 trend](data/chart-history/2026-08-14.png)

**2026-08-13**
![2026-08-13 trend](data/chart-history/2026-08-13.png)

**2026-08-12**
![2026-08-12 trend](data/chart-history/2026-08-12.png)

**2026-08-11**
![2026-08-11 trend](data/chart-history/2026-08-11.png)

**2026-08-10**
![2026-08-10 trend](data/chart-history/2026-08-10.png)

**2026-08-09**
![2026-08-09 trend](data/chart-history/2026-08-09.png)

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
