# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-11 13:30:34 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 28.0 °C |
| 💧 Humidity | 91 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 3.0 km/h |
| 🧭 Wind Direction | 287° |
| 🔵 Pressure | 975.8 hPa |
| 🌫️ AQI (US) | 109 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 34.1 µg/m³ |
| PM10 | 34.6 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-11 13:30:34 | 28.0 | 0.0 | 109 | 3.0 | 91 |
| 2026-08-11 12:30:39 | 28.7 | 0.0 | 111 | 3.2 | 87 |
| 2026-08-11 11:30:29 | 30.2 | 0.0 | 112 | 8.4 | 79 |
| 2026-08-11 10:30:34 | 30.8 | 0.0 | 111 | 7.5 | 75 |
| 2026-08-11 09:30:35 | 30.8 | 0.1 | 111 | 6.0 | 76 |
| 2026-08-11 08:30:30 | 30.4 | 0.1 | 112 | 5.3 | 82 |
| 2026-08-11 07:30:32 | 30.2 | 0.0 | 112 | 5.9 | 85 |
| 2026-08-11 06:30:29 | 29.7 | 0.0 | 113 | 7.1 | 84 |
| 2026-08-11 05:30:27 | 28.7 | 0.0 | 114 | 7.4 | 86 |
| 2026-08-11 04:30:33 | 27.7 | 0.1 | 115 | 6.8 | 89 |
| 2026-08-11 03:30:31 | 26.7 | 0.2 | 116 | 6.2 | 92 |
| 2026-08-11 02:30:30 | 26.2 | 0.0 | 116 | 8.4 | 95 |
| 2026-08-11 01:30:30 | 26.2 | 0.2 | 117 | 9.4 | 95 |
| 2026-08-11 00:30:30 | 26.0 | 0.3 | 116 | 8.3 | 96 |
| 2026-08-10 23:30:31 | 26.2 | 0.0 | 116 | 8.3 | 97 |
| 2026-08-10 22:30:29 | 26.6 | 0.0 | 101 | 9.1 | 96 |
| 2026-08-10 21:30:36 | 26.9 | 0.0 | 101 | 8.5 | 96 |
| 2026-08-10 20:30:39 | 27.1 | 0.0 | 101 | 7.0 | 97 |
| 2026-08-10 19:30:38 | 27.3 | 0.0 | 100 | 7.8 | 96 |
| 2026-08-10 18:30:39 | 27.3 | 0.0 | 99 | 8.6 | 95 |
| 2026-08-10 17:30:31 | 27.4 | 0.3 | 98 | 8.2 | 95 |
| 2026-08-10 16:30:32 | 27.6 | 0.2 | 105 | 6.9 | 93 |
| 2026-08-10 15:30:34 | 27.8 | 0.0 | 116 | 5.8 | 92 |
| 2026-08-10 14:30:31 | 28.0 | 0.0 | 120 | 6.1 | 90 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 3 day(s)</summary>

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
