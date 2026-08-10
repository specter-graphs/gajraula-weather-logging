# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-10 18:30:39 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 27.3 °C |
| 💧 Humidity | 95 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 8.6 km/h |
| 🧭 Wind Direction | 82° |
| 🔵 Pressure | 977.5 hPa |
| 🌫️ AQI (US) | 99 — Moderate 🟡 |
| PM2.5 | 46.7 µg/m³ |
| PM10 | 47.4 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
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
| 2026-08-10 01:30:30 | 27.9 | 0.0 | 92 | 8.5 | 89 |
| 2026-08-10 00:30:28 | 27.5 | 0.0 | 93 | 10.9 | 90 |
| 2026-08-09 23:30:29 | 27.7 | 0.0 | 93 | 8.8 | 90 |
| 2026-08-09 22:30:29 | 27.8 | 0.0 | 93 | 7.6 | 89 |
| 2026-08-09 21:30:32 | 28.0 | 0.0 | 103 | 9.7 | 88 |
| 2026-08-09 20:30:27 | 28.4 | 0.0 | 100 | 9.1 | 87 |
| 2026-08-09 19:30:28 | 28.8 | 0.0 | 97 | 8.0 | 85 |

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
