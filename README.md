# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-21 23:30:31 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 24.9 °C |
| 💧 Humidity | 97 % |
| 🌧️ Rain (last hr) | 0.2 mm |
| 💨 Wind Speed | 5.9 km/h |
| 🧭 Wind Direction | 203° |
| 🔵 Pressure | 978.3 hPa |
| 🌫️ AQI (US) | 143 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 83.8 µg/m³ |
| PM10 | 107.8 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-21 23:30:31 | 24.9 | 0.2 | 143 | 5.9 | 97 |
| 2026-08-21 22:30:34 | 25.6 | 0.0 | 139 | 5.3 | 96 |
| 2026-08-21 21:30:30 | 25.4 | 0.1 | 128 | 5.8 | 94 |
| 2026-08-21 20:30:32 | 26.3 | 0.2 | 126 | 10.4 | 88 |
| 2026-08-21 19:30:33 | 27.9 | 0.0 | 124 | 8.8 | 85 |
| 2026-08-21 18:30:30 | 27.7 | 0.0 | 122 | 3.4 | 92 |
| 2026-08-21 17:30:33 | 27.9 | 0.0 | 121 | 3.9 | 91 |
| 2026-08-21 16:30:31 | 28.3 | 0.0 | 121 | 4.5 | 88 |
| 2026-08-21 15:30:31 | 28.8 | 0.0 | 131 | 6.3 | 85 |
| 2026-08-21 14:30:33 | 29.4 | 0.0 | 140 | 6.5 | 82 |
| 2026-08-21 13:30:34 | 30.1 | 0.0 | 142 | 4.5 | 81 |
| 2026-08-21 12:30:30 | 31.2 | 0.0 | 136 | 6.1 | 76 |
| 2026-08-21 11:30:30 | 32.6 | 0.0 | 123 | 7.3 | 69 |
| 2026-08-21 10:30:32 | 33.1 | 0.0 | 116 | 9.2 | 66 |
| 2026-08-21 09:30:34 | 33.4 | 0.0 | 119 | 9.1 | 65 |
| 2026-08-21 08:30:31 | 33.3 | 0.0 | 116 | 8.9 | 66 |
| 2026-08-21 07:30:31 | 32.8 | 0.0 | 113 | 10.2 | 69 |
| 2026-08-21 06:30:38 | 32.1 | 0.0 | 111 | 5.5 | 74 |
| 2026-08-21 05:30:42 | 31.5 | 0.0 | 109 | 7.2 | 76 |
| 2026-08-21 04:30:32 | 30.7 | 0.0 | 108 | 7.5 | 80 |
| 2026-08-21 03:30:28 | 29.7 | 0.0 | 107 | 5.7 | 83 |
| 2026-08-21 02:30:35 | 28.7 | 0.0 | 105 | 5.1 | 88 |
| 2026-08-21 01:30:32 | 27.8 | 0.0 | 103 | 5.0 | 94 |
| 2026-08-21 00:30:28 | 27.1 | 0.0 | 100 | 3.9 | 98 |

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
