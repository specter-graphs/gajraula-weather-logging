# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-10 10:30:36 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 30.2 °C |
| 💧 Humidity | 78 % |
| 🌧️ Rain (last hr) | 0.1 mm |
| 💨 Wind Speed | 5.4 km/h |
| 🧭 Wind Direction | 86° |
| 🔵 Pressure | 974.8 hPa |
| 🌫️ AQI (US) | 93 — Moderate 🟡 |
| PM2.5 | 32.6 µg/m³ |
| PM10 | 33.3 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
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
| 2026-08-09 18:30:30 | 28.7 | 0.0 | 95 | 8.7 | 84 |
| 2026-08-09 17:30:28 | 28.9 | 0.0 | 94 | 7.1 | 84 |
| 2026-08-09 16:30:31 | 29.1 | 0.0 | 115 | 5.8 | 84 |
| 2026-08-09 15:30:32 | 29.5 | 0.0 | 137 | 6.5 | 82 |
| 2026-08-09 14:30:32 | 29.9 | 0.0 | 151 | 6.4 | 82 |
| 2026-08-09 13:30:34 | 30.6 | 0.0 | 154 | 5.6 | 80 |
| 2026-08-09 12:30:30 | 31.9 | 0.0 | 149 | 5.7 | 73 |
| 2026-08-09 11:30:31 | 32.6 | 0.0 | 135 | 5.2 | 68 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 2 day(s)</summary>

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
