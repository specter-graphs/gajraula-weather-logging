# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-18 23:30:30 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 26.2 °C |
| 💧 Humidity | 99 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 1.3 km/h |
| 🧭 Wind Direction | 262° |
| 🔵 Pressure | 978.9 hPa |
| 🌫️ AQI (US) | 133 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 77.3 µg/m³ |
| PM10 | 89.6 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-18 23:30:30 | 26.2 | 0.0 | 133 | 1.3 | 99 |
| 2026-08-18 22:30:31 | 26.5 | 0.0 | 129 | 1.3 | 98 |
| 2026-08-18 21:30:29 | 26.5 | 0.0 | 106 | 2.0 | 98 |
| 2026-08-18 19:30:32 | 26.6 | 0.0 | 110 | 3.3 | 96 |
| 2026-08-18 18:30:31 | 26.5 | 0.0 | 115 | 2.1 | 96 |
| 2026-08-18 17:30:33 | 26.6 | 0.0 | 119 | 2.9 | 95 |
| 2026-08-18 16:30:35 | 26.7 | 0.0 | 124 | 3.4 | 94 |
| 2026-08-18 15:30:32 | 26.9 | 0.0 | 128 | 2.4 | 93 |
| 2026-08-18 14:30:38 | 27.3 | 0.0 | 130 | 5.4 | 93 |
| 2026-08-18 13:30:32 | 28.0 | 0.0 | 133 | 3.8 | 90 |
| 2026-08-18 12:30:33 | 27.1 | 0.0 | 136 | 3.3 | 89 |
| 2026-08-18 11:30:34 | 29.9 | 0.0 | 137 | 4.8 | 76 |
| 2026-08-18 10:30:33 | 31.5 | 0.0 | 135 | 4.5 | 72 |
| 2026-08-18 09:30:37 | 31.3 | 0.0 | 136 | 2.1 | 72 |
| 2026-08-18 08:30:29 | 30.8 | 0.1 | 138 | 1.0 | 75 |
| 2026-08-18 07:30:33 | 30.3 | 0.0 | 140 | 1.9 | 76 |
| 2026-08-18 06:30:31 | 29.9 | 0.1 | 143 | 3.5 | 77 |
| 2026-08-18 05:30:29 | 29.2 | 0.0 | 147 | 2.7 | 78 |
| 2026-08-18 04:30:28 | 28.2 | 0.0 | 150 | 0.2 | 81 |
| 2026-08-18 03:30:32 | 27.4 | 0.0 | 152 | 0.6 | 86 |
| 2026-08-18 02:30:29 | 26.4 | 0.0 | 153 | 1.5 | 90 |
| 2026-08-18 01:30:32 | 25.4 | 0.0 | 155 | 0.4 | 94 |
| 2026-08-18 00:30:31 | 25.2 | 0.0 | 157 | 1.1 | 96 |
| 2026-08-17 23:30:32 | 25.3 | 0.1 | 158 | 2.8 | 96 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 7 day(s)</summary>

**2026-08-18**
![2026-08-18 trend](data/chart-history/2026-08-18.png)

**2026-08-17**
![2026-08-17 trend](data/chart-history/2026-08-17.png)

**2026-08-16**
![2026-08-16 trend](data/chart-history/2026-08-16.png)

**2026-08-15**
![2026-08-15 trend](data/chart-history/2026-08-15.png)

**2026-08-14**
![2026-08-14 trend](data/chart-history/2026-08-14.png)

**2026-08-13**
![2026-08-13 trend](data/chart-history/2026-08-13.png)

**2026-08-12**
![2026-08-12 trend](data/chart-history/2026-08-12.png)

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
