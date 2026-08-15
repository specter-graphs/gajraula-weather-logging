# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-15 13:30:29 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 29.9 °C |
| 💧 Humidity | 83 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 5.1 km/h |
| 🧭 Wind Direction | 278° |
| 🔵 Pressure | 975.8 hPa |
| 🌫️ AQI (US) | 131 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 38.0 µg/m³ |
| PM10 | 42.0 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-15 13:30:29 | 29.9 | 0.0 | 131 | 5.1 | 83 |
| 2026-08-15 12:30:29 | 31.3 | 0.0 | 124 | 7.2 | 78 |
| 2026-08-15 11:30:31 | 32.0 | 0.0 | 109 | 10.7 | 74 |
| 2026-08-15 10:30:29 | 32.6 | 0.0 | 103 | 11.3 | 73 |
| 2026-08-15 09:30:31 | 32.9 | 0.0 | 102 | 9.6 | 73 |
| 2026-08-15 08:30:36 | 32.6 | 0.0 | 101 | 8.9 | 72 |
| 2026-08-15 07:30:31 | 32.0 | 0.0 | 100 | 7.7 | 74 |
| 2026-08-15 06:30:30 | 32.0 | 0.0 | 100 | 6.3 | 72 |
| 2026-08-15 05:30:31 | 31.0 | 0.0 | 100 | 3.5 | 77 |
| 2026-08-15 04:30:35 | 30.0 | 0.0 | 100 | 1.8 | 81 |
| 2026-08-15 03:33:03 | 28.8 | 0.0 | 100 | 2.8 | 85 |
| 2026-08-15 02:31:36 | 27.8 | 0.0 | 99 | 3.7 | 90 |
| 2026-08-15 01:30:35 | 27.4 | 0.0 | 98 | 5.0 | 93 |
| 2026-08-15 00:31:20 | 26.4 | 0.0 | 96 | 3.7 | 99 |
| 2026-08-14 23:30:30 | 26.4 | 0.0 | 97 | 3.8 | 97 |
| 2026-08-14 22:30:31 | 26.6 | 0.0 | 108 | 3.1 | 97 |
| 2026-08-14 21:30:28 | 26.8 | 0.0 | 108 | 2.6 | 96 |
| 2026-08-14 20:30:30 | 26.9 | 0.0 | 109 | 2.8 | 95 |
| 2026-08-14 19:30:31 | 27.1 | 0.0 | 109 | 0.4 | 95 |
| 2026-08-14 18:30:29 | 26.8 | 0.0 | 108 | 1.1 | 95 |
| 2026-08-14 17:30:31 | 27.0 | 0.0 | 107 | 2.8 | 95 |
| 2026-08-14 16:30:33 | 27.2 | 0.0 | 108 | 4.8 | 93 |
| 2026-08-14 15:30:34 | 27.5 | 0.0 | 110 | 5.1 | 92 |
| 2026-08-14 14:30:29 | 27.7 | 0.0 | 112 | 4.5 | 91 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 7 day(s)</summary>

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
