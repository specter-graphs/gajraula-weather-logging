# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-12 04:30:28 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 31.2 °C |
| 💧 Humidity | 74 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 6.3 km/h |
| 🧭 Wind Direction | 325° |
| 🔵 Pressure | 978.7 hPa |
| 🌫️ AQI (US) | 136 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 39.1 µg/m³ |
| PM10 | 39.3 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-12 04:30:28 | 31.2 | 0.0 | 136 | 6.3 | 74 |
| 2026-08-12 03:30:29 | 29.9 | 0.0 | 132 | 6.6 | 82 |
| 2026-08-12 02:30:33 | 28.3 | 0.0 | 127 | 5.3 | 90 |
| 2026-08-12 01:30:33 | 26.8 | 0.0 | 121 | 4.9 | 96 |
| 2026-08-12 00:30:33 | 25.8 | 0.0 | 116 | 4.1 | 99 |
| 2026-08-11 23:30:43 | 25.7 | 0.0 | 112 | 3.5 | 100 |
| 2026-08-11 22:30:35 | 25.8 | 0.0 | 149 | 3.2 | 100 |
| 2026-08-11 21:30:32 | 25.9 | 0.0 | 138 | 3.0 | 99 |
| 2026-08-11 20:30:38 | 26.3 | 0.0 | 128 | 3.4 | 99 |
| 2026-08-11 19:30:32 | 26.5 | 0.0 | 119 | 4.1 | 99 |
| 2026-08-11 18:30:33 | 26.3 | 0.0 | 112 | 4.6 | 98 |
| 2026-08-11 17:30:40 | 26.5 | 0.0 | 108 | 2.2 | 98 |
| 2026-08-11 16:30:40 | 26.9 | 0.0 | 106 | 0.9 | 96 |
| 2026-08-11 15:30:40 | 27.1 | 0.0 | 106 | 1.1 | 95 |
| 2026-08-11 14:30:31 | 27.3 | 0.0 | 107 | 1.7 | 95 |
| 2026-08-11 13:30:34 | 28.0 | 0.0 | 109 | 3.0 | 91 |
| 2026-08-11 12:30:39 | 28.7 | 0.0 | 111 | 3.2 | 87 |
| 2026-08-11 11:30:29 | 30.2 | 0.0 | 112 | 8.4 | 79 |
| 2026-08-11 10:30:34 | 30.8 | 0.0 | 111 | 7.5 | 75 |
| 2026-08-11 09:30:35 | 30.8 | 0.1 | 111 | 6.0 | 76 |
| 2026-08-11 08:30:30 | 30.4 | 0.1 | 112 | 5.3 | 82 |
| 2026-08-11 07:30:32 | 30.2 | 0.0 | 112 | 5.9 | 85 |
| 2026-08-11 06:30:29 | 29.7 | 0.0 | 113 | 7.1 | 84 |
| 2026-08-11 05:30:27 | 28.7 | 0.0 | 114 | 7.4 | 86 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 4 day(s)</summary>

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
