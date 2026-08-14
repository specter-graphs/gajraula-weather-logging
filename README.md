# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-14 17:30:31 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 27.0 °C |
| 💧 Humidity | 95 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 2.8 km/h |
| 🧭 Wind Direction | 135° |
| 🔵 Pressure | 979.2 hPa |
| 🌫️ AQI (US) | 107 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 56.3 µg/m³ |
| PM10 | 56.6 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-14 17:30:31 | 27.0 | 0.0 | 107 | 2.8 | 95 |
| 2026-08-14 16:30:33 | 27.2 | 0.0 | 108 | 4.8 | 93 |
| 2026-08-14 15:30:34 | 27.5 | 0.0 | 110 | 5.1 | 92 |
| 2026-08-14 14:30:29 | 27.7 | 0.0 | 112 | 4.5 | 91 |
| 2026-08-14 13:30:30 | 28.3 | 0.0 | 115 | 3.3 | 88 |
| 2026-08-14 12:30:32 | 29.7 | 0.0 | 117 | 5.4 | 83 |
| 2026-08-14 11:30:31 | 30.0 | 0.1 | 119 | 5.6 | 80 |
| 2026-08-14 10:30:32 | 30.2 | 0.0 | 121 | 5.2 | 80 |
| 2026-08-14 09:30:36 | 30.4 | 0.0 | 123 | 6.4 | 80 |
| 2026-08-14 08:30:28 | 30.5 | 0.0 | 123 | 6.9 | 79 |
| 2026-08-14 07:30:29 | 30.2 | 0.1 | 123 | 8.0 | 78 |
| 2026-08-14 06:30:30 | 30.7 | 0.0 | 124 | 5.0 | 79 |
| 2026-08-14 05:30:36 | 29.5 | 0.1 | 125 | 6.8 | 81 |
| 2026-08-14 04:30:33 | 28.3 | 0.1 | 127 | 10.2 | 86 |
| 2026-08-14 03:30:29 | 27.7 | 0.0 | 131 | 10.2 | 90 |
| 2026-08-14 02:30:27 | 27.6 | 0.0 | 137 | 7.6 | 90 |
| 2026-08-14 01:30:32 | 27.0 | 0.0 | 143 | 9.0 | 92 |
| 2026-08-14 00:30:34 | 27.2 | 0.1 | 149 | 8.3 | 96 |
| 2026-08-13 23:30:31 | 26.5 | 0.1 | 149 | 7.9 | 97 |
| 2026-08-13 22:30:29 | 27.1 | 0.3 | 148 | 5.5 | 96 |
| 2026-08-13 21:30:30 | 27.9 | 0.1 | 154 | 6.6 | 95 |
| 2026-08-13 20:30:35 | 28.3 | 0.0 | 154 | 1.8 | 95 |
| 2026-08-13 19:30:34 | 28.5 | 0.0 | 154 | 1.8 | 94 |
| 2026-08-13 18:30:50 | 29.0 | 0.0 | 154 | 2.6 | 94 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 6 day(s)</summary>

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
