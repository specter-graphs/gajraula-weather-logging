# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-23 06:30:29 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 30.4 °C |
| 💧 Humidity | 75 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 2.3 km/h |
| 🧭 Wind Direction | 299° |
| 🔵 Pressure | 980.7 hPa |
| 🌫️ AQI (US) | 117 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 36.6 µg/m³ |
| PM10 | 42.0 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-23 06:30:29 | 30.4 | 0.0 | 117 | 2.3 | 75 |
| 2026-08-23 05:30:27 | 29.8 | 0.0 | 115 | 1.9 | 77 |
| 2026-08-23 04:30:29 | 28.9 | 0.0 | 114 | 1.6 | 81 |
| 2026-08-23 03:30:34 | 27.5 | 0.0 | 112 | 2.0 | 87 |
| 2026-08-23 02:30:29 | 25.7 | 0.2 | 109 | 1.2 | 94 |
| 2026-08-23 01:30:30 | 24.5 | 0.5 | 105 | 1.1 | 97 |
| 2026-08-23 00:30:31 | 24.5 | 0.3 | 102 | 3.6 | 96 |
| 2026-08-22 23:30:30 | 25.6 | 0.1 | 104 | 6.2 | 97 |
| 2026-08-22 22:30:30 | 25.7 | 0.0 | 106 | 5.5 | 98 |
| 2026-08-22 21:30:31 | 25.8 | 0.0 | 119 | 5.6 | 98 |
| 2026-08-22 20:30:30 | 25.5 | 0.2 | 119 | 3.7 | 99 |
| 2026-08-22 19:30:28 | 26.2 | 0.2 | 119 | 0.4 | 98 |
| 2026-08-22 18:30:35 | 26.5 | 0.0 | 120 | 2.9 | 98 |
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

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 7 day(s)</summary>

**2026-08-22**
![2026-08-22 trend](data/chart-history/2026-08-22.png)

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
