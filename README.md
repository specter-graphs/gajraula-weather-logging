# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-11 01:30:30 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 26.2 °C |
| 💧 Humidity | 95 % |
| 🌧️ Rain (last hr) | 0.2 mm |
| 💨 Wind Speed | 9.4 km/h |
| 🧭 Wind Direction | 114° |
| 🔵 Pressure | 978.5 hPa |
| 🌫️ AQI (US) | 117 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 27.5 µg/m³ |
| PM10 | 27.9 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
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
| 2026-08-10 13:30:48 | 28.4 | 0.0 | 115 | 7.5 | 89 |
| 2026-08-10 12:30:34 | 29.0 | 0.0 | 102 | 9.1 | 89 |
| 2026-08-10 11:30:29 | 29.6 | 0.1 | 94 | 7.0 | 83 |
| 2026-08-10 10:30:36 | 30.2 | 0.1 | 93 | 5.4 | 78 |
| 2026-08-10 09:30:35 | 30.3 | 0.0 | 92 | 5.6 | 79 |
| 2026-08-10 08:30:31 | 30.1 | 0.0 | 91 | 7.2 | 86 |
| 2026-08-10 07:30:26 | 29.3 | 0.1 | 90 | 5.2 | 91 |
| 2026-08-10 06:30:37 | 31.8 | 0.0 | 90 | 6.9 | 77 |
| 2026-08-10 05:30:38 | 31.3 | 0.0 | 90 | 7.9 | 78 |
| 2026-08-10 04:30:29 | 30.7 | 0.0 | 89 | 9.5 | 80 |
| 2026-08-10 03:30:32 | 29.6 | 0.0 | 90 | 10.5 | 83 |
| 2026-08-10 02:30:33 | 28.6 | 0.0 | 91 | 9.5 | 86 |

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
