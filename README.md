# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-15 20:30:31 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 27.0 °C |
| 💧 Humidity | 91 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 6.4 km/h |
| 🧭 Wind Direction | 140° |
| 🔵 Pressure | 977.2 hPa |
| 🌫️ AQI (US) | 120 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 52.7 µg/m³ |
| PM10 | 54.7 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-15 20:30:31 | 27.0 | 0.0 | 120 | 6.4 | 91 |
| 2026-08-15 19:30:32 | 26.3 | 0.0 | 118 | 5.2 | 99 |
| 2026-08-15 18:30:35 | 27.5 | 0.1 | 116 | 5.5 | 93 |
| 2026-08-15 17:30:35 | 28.3 | 0.0 | 114 | 3.0 | 92 |
| 2026-08-15 16:30:32 | 28.7 | 0.0 | 112 | 1.5 | 89 |
| 2026-08-15 15:30:28 | 29.1 | 0.0 | 121 | 1.0 | 87 |
| 2026-08-15 14:30:31 | 29.2 | 0.0 | 130 | 2.9 | 86 |
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
