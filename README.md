# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-22 17:30:30 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 26.8 °C |
| 💧 Humidity | 97 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 3.9 km/h |
| 🧭 Wind Direction | 152° |
| 🔵 Pressure | 978.9 hPa |
| 🌫️ AQI (US) | 120 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 65.4 µg/m³ |
| PM10 | 70.5 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-22 17:30:30 | 26.8 | 0.0 | 120 | 3.9 | 97 |
| 2026-08-22 16:30:31 | 27.1 | 0.0 | 120 | 4.0 | 97 |
| 2026-08-22 15:30:30 | 27.6 | 0.0 | 122 | 4.0 | 95 |
| 2026-08-22 14:30:28 | 28.0 | 0.0 | 123 | 2.8 | 94 |
| 2026-08-22 13:30:30 | 28.7 | 0.1 | 126 | 2.7 | 90 |
| 2026-08-22 12:30:32 | 29.5 | 0.0 | 128 | 4.5 | 85 |
| 2026-08-22 11:30:28 | 32.0 | 0.0 | 130 | 7.2 | 72 |
| 2026-08-22 10:30:31 | 32.2 | 0.0 | 131 | 8.7 | 69 |
| 2026-08-22 09:30:29 | 32.7 | 0.0 | 146 | 10.7 | 67 |
| 2026-08-22 08:30:31 | 33.0 | 0.0 | 148 | 10.5 | 66 |
| 2026-08-22 07:30:32 | 32.5 | 0.0 | 149 | 9.4 | 69 |
| 2026-08-22 06:30:34 | 30.7 | 0.0 | 150 | 4.6 | 74 |
| 2026-08-22 05:30:32 | 29.9 | 0.0 | 150 | 5.3 | 76 |
| 2026-08-22 04:30:31 | 28.6 | 0.0 | 151 | 7.6 | 81 |
| 2026-08-22 03:30:29 | 27.1 | 0.0 | 150 | 8.6 | 89 |
| 2026-08-22 02:30:31 | 26.0 | 0.1 | 150 | 9.6 | 93 |
| 2026-08-22 01:30:31 | 26.1 | 0.2 | 149 | 10.1 | 93 |
| 2026-08-22 00:30:29 | 26.4 | 0.0 | 146 | 7.0 | 94 |
| 2026-08-21 23:30:31 | 24.9 | 0.2 | 143 | 5.9 | 97 |
| 2026-08-21 22:30:34 | 25.6 | 0.0 | 139 | 5.3 | 96 |
| 2026-08-21 21:30:30 | 25.4 | 0.1 | 128 | 5.8 | 94 |
| 2026-08-21 20:30:32 | 26.3 | 0.2 | 126 | 10.4 | 88 |
| 2026-08-21 19:30:33 | 27.9 | 0.0 | 124 | 8.8 | 85 |
| 2026-08-21 18:30:30 | 27.7 | 0.0 | 122 | 3.4 | 92 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 7 day(s)</summary>

**2026-08-21**
![2026-08-21 trend](data/chart-history/2026-08-21.png)

**2026-08-20**
![2026-08-20 trend](data/chart-history/2026-08-20.png)

**2026-08-19**
![2026-08-19 trend](data/chart-history/2026-08-19.png)

**2026-08-18**
![2026-08-18 trend](data/chart-history/2026-08-18.png)

**2026-08-17**
![2026-08-17 trend](data/chart-history/2026-08-17.png)

**2026-08-16**
![2026-08-16 trend](data/chart-history/2026-08-16.png)

**2026-08-15**
![2026-08-15 trend](data/chart-history/2026-08-15.png)

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
