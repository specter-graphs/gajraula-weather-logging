# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-14 02:30:27 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 27.6 °C |
| 💧 Humidity | 90 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 7.6 km/h |
| 🧭 Wind Direction | 117° |
| 🔵 Pressure | 978.8 hPa |
| 🌫️ AQI (US) | 137 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 35.2 µg/m³ |
| PM10 | 36.7 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-14 02:30:27 | 27.6 | 0.0 | 137 | 7.6 | 90 |
| 2026-08-14 01:30:32 | 27.0 | 0.0 | 143 | 9.0 | 92 |
| 2026-08-14 00:30:34 | 27.2 | 0.1 | 149 | 8.3 | 96 |
| 2026-08-13 23:30:31 | 26.5 | 0.1 | 149 | 7.9 | 97 |
| 2026-08-13 22:30:29 | 27.1 | 0.3 | 148 | 5.5 | 96 |
| 2026-08-13 21:30:30 | 27.9 | 0.1 | 154 | 6.6 | 95 |
| 2026-08-13 20:30:35 | 28.3 | 0.0 | 154 | 1.8 | 95 |
| 2026-08-13 19:30:34 | 28.5 | 0.0 | 154 | 1.8 | 94 |
| 2026-08-13 18:30:50 | 29.0 | 0.0 | 154 | 2.6 | 94 |
| 2026-08-13 17:30:35 | 29.2 | 0.0 | 155 | 2.3 | 92 |
| 2026-08-13 16:30:35 | 29.5 | 0.0 | 155 | 1.7 | 91 |
| 2026-08-13 15:30:32 | 29.7 | 0.0 | 155 | 2.6 | 90 |
| 2026-08-13 14:30:35 | 30.0 | 0.0 | 163 | 2.3 | 88 |
| 2026-08-13 13:30:34 | 30.6 | 0.0 | 171 | 3.8 | 85 |
| 2026-08-13 12:30:32 | 31.4 | 0.0 | 173 | 8.3 | 80 |
| 2026-08-13 11:30:30 | 32.2 | 0.0 | 168 | 4.9 | 74 |
| 2026-08-13 10:30:31 | 31.2 | 0.1 | 164 | 4.5 | 80 |
| 2026-08-13 09:30:32 | 31.6 | 0.2 | 150 | 8.4 | 77 |
| 2026-08-13 08:30:31 | 33.6 | 0.0 | 148 | 8.4 | 67 |
| 2026-08-13 07:30:28 | 34.2 | 0.0 | 145 | 8.8 | 65 |
| 2026-08-13 06:30:28 | 33.7 | 0.0 | 143 | 5.6 | 67 |
| 2026-08-13 05:30:36 | 33.4 | 0.0 | 140 | 4.0 | 65 |
| 2026-08-13 04:30:31 | 32.7 | 0.0 | 138 | 3.6 | 71 |
| 2026-08-13 03:30:33 | 31.5 | 0.0 | 135 | 5.1 | 79 |

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
