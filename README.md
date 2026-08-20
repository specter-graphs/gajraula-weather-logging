# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-20 15:30:36 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 28.3 °C |
| 💧 Humidity | 96 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 1.5 km/h |
| 🧭 Wind Direction | 166° |
| 🔵 Pressure | 979.2 hPa |
| 🌫️ AQI (US) | 123 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 38.8 µg/m³ |
| PM10 | 40.5 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-20 15:30:36 | 28.3 | 0.0 | 123 | 1.5 | 96 |
| 2026-08-20 14:30:31 | 28.6 | 0.0 | 136 | 1.8 | 95 |
| 2026-08-20 13:30:41 | 29.2 | 0.0 | 138 | 2.6 | 91 |
| 2026-08-20 12:30:32 | 29.8 | 0.0 | 129 | 4.0 | 87 |
| 2026-08-20 11:30:32 | 30.7 | 0.0 | 114 | 7.1 | 80 |
| 2026-08-20 10:30:33 | 31.0 | 0.0 | 116 | 4.4 | 77 |
| 2026-08-20 09:30:31 | 31.0 | 0.0 | 117 | 3.9 | 77 |
| 2026-08-20 08:30:36 | 31.2 | 0.0 | 118 | 4.6 | 77 |
| 2026-08-20 07:30:34 | 31.6 | 0.0 | 120 | 4.0 | 76 |
| 2026-08-20 06:30:32 | 32.0 | 0.0 | 121 | 0.6 | 72 |
| 2026-08-20 05:30:29 | 31.3 | 0.0 | 122 | 2.6 | 75 |
| 2026-08-20 04:30:29 | 30.6 | 0.0 | 123 | 4.2 | 79 |
| 2026-08-20 03:30:30 | 29.5 | 0.0 | 123 | 5.1 | 83 |
| 2026-08-20 02:30:31 | 28.4 | 0.0 | 123 | 5.7 | 90 |
| 2026-08-20 01:30:33 | 27.3 | 0.0 | 121 | 5.2 | 96 |
| 2026-08-20 00:30:30 | 26.1 | 0.0 | 119 | 2.1 | 100 |
| 2026-08-19 23:30:30 | 26.1 | 0.0 | 122 | 2.6 | 98 |
| 2026-08-19 22:30:35 | 26.2 | 0.0 | 124 | 3.6 | 98 |
| 2026-08-19 21:30:32 | 26.3 | 0.0 | 128 | 3.5 | 97 |
| 2026-08-19 20:30:31 | 26.4 | 0.0 | 130 | 3.0 | 97 |
| 2026-08-19 19:30:32 | 26.5 | 0.0 | 132 | 2.8 | 97 |
| 2026-08-19 18:30:31 | 26.8 | 0.0 | 135 | 2.9 | 95 |
| 2026-08-19 17:30:32 | 26.8 | 0.0 | 137 | 4.1 | 95 |
| 2026-08-19 16:30:33 | 26.9 | 0.1 | 139 | 4.8 | 96 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 7 day(s)</summary>

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

**2026-08-14**
![2026-08-14 trend](data/chart-history/2026-08-14.png)

**2026-08-13**
![2026-08-13 trend](data/chart-history/2026-08-13.png)

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
