# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-13 05:30:36 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 33.4 °C |
| 💧 Humidity | 65 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 4.0 km/h |
| 🧭 Wind Direction | 238° |
| 🔵 Pressure | 979.1 hPa |
| 🌫️ AQI (US) | 140 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 48.4 µg/m³ |
| PM10 | 51.0 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-13 05:30:36 | 33.4 | 0.0 | 140 | 4.0 | 65 |
| 2026-08-13 04:30:31 | 32.7 | 0.0 | 138 | 3.6 | 71 |
| 2026-08-13 03:30:33 | 31.5 | 0.0 | 135 | 5.1 | 79 |
| 2026-08-13 02:30:30 | 29.9 | 0.0 | 134 | 5.5 | 86 |
| 2026-08-13 01:30:31 | 28.5 | 0.0 | 134 | 6.3 | 90 |
| 2026-08-13 00:30:38 | 27.5 | 0.0 | 135 | 5.1 | 93 |
| 2026-08-12 23:30:34 | 27.6 | 0.0 | 137 | 8.1 | 92 |
| 2026-08-12 22:30:31 | 27.5 | 0.0 | 154 | 4.9 | 93 |
| 2026-08-12 21:30:31 | 27.6 | 0.0 | 152 | 4.0 | 93 |
| 2026-08-12 20:30:31 | 27.9 | 0.0 | 149 | 4.4 | 91 |
| 2026-08-12 19:30:36 | 28.3 | 0.0 | 142 | 5.7 | 89 |
| 2026-08-12 18:30:32 | 28.8 | 0.0 | 137 | 4.7 | 88 |
| 2026-08-12 17:30:34 | 29.2 | 0.0 | 133 | 4.2 | 85 |
| 2026-08-12 16:30:32 | 30.0 | 0.0 | 130 | 2.1 | 80 |
| 2026-08-12 15:30:32 | 31.0 | 0.0 | 127 | 0.4 | 76 |
| 2026-08-12 14:30:34 | 31.6 | 0.0 | 125 | 0.2 | 74 |
| 2026-08-12 13:30:31 | 32.6 | 0.0 | 124 | 0.9 | 70 |
| 2026-08-12 12:30:33 | 33.2 | 0.0 | 124 | 2.3 | 64 |
| 2026-08-12 11:30:29 | 33.8 | 0.0 | 125 | 2.7 | 64 |
| 2026-08-12 10:30:33 | 34.0 | 0.0 | 125 | 3.9 | 63 |
| 2026-08-12 09:30:38 | 34.1 | 0.0 | 138 | 4.8 | 62 |
| 2026-08-12 08:30:31 | 34.1 | 0.0 | 138 | 5.2 | 62 |
| 2026-08-12 07:30:34 | 33.7 | 0.0 | 138 | 5.5 | 64 |
| 2026-08-12 06:30:32 | 32.9 | 0.0 | 138 | 6.1 | 65 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 5 day(s)</summary>

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
