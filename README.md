# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-17 09:30:33 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 32.4 °C |
| 💧 Humidity | 75 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 9.2 km/h |
| 🧭 Wind Direction | 250° |
| 🔵 Pressure | 976.1 hPa |
| 🌫️ AQI (US) | 150 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 62.6 µg/m³ |
| PM10 | 159.3 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-17 09:30:33 | 32.4 | 0.0 | 150 | 9.2 | 75 |
| 2026-08-17 08:30:30 | 32.3 | 0.0 | 150 | 7.4 | 75 |
| 2026-08-17 07:30:36 | 32.0 | 0.0 | 150 | 7.6 | 74 |
| 2026-08-17 06:30:30 | 31.4 | 0.0 | 150 | 6.7 | 77 |
| 2026-08-17 05:30:30 | 30.9 | 0.0 | 149 | 6.7 | 79 |
| 2026-08-17 04:30:29 | 30.3 | 0.0 | 148 | 7.6 | 79 |
| 2026-08-17 03:30:31 | 29.4 | 0.0 | 147 | 7.1 | 82 |
| 2026-08-17 02:30:30 | 28.2 | 0.0 | 146 | 3.1 | 89 |
| 2026-08-17 01:30:29 | 26.6 | 0.0 | 144 | 2.2 | 97 |
| 2026-08-17 00:30:32 | 26.1 | 0.0 | 142 | 3.0 | 98 |
| 2026-08-16 23:30:28 | 26.0 | 0.0 | 140 | 2.6 | 98 |
| 2026-08-16 22:30:29 | 26.1 | 0.0 | 122 | 2.4 | 98 |
| 2026-08-16 21:30:29 | 26.1 | 0.0 | 123 | 2.1 | 99 |
| 2026-08-16 20:30:32 | 25.9 | 0.0 | 126 | 3.1 | 100 |
| 2026-08-16 19:30:28 | 25.9 | 0.0 | 130 | 1.8 | 97 |
| 2026-08-16 18:30:32 | 26.0 | 0.0 | 133 | 4.0 | 97 |
| 2026-08-16 17:30:30 | 26.2 | 0.0 | 136 | 5.4 | 97 |
| 2026-08-16 16:30:32 | 26.5 | 0.0 | 137 | 7.2 | 97 |
| 2026-08-16 15:30:30 | 26.8 | 0.0 | 138 | 5.5 | 98 |
| 2026-08-16 14:30:31 | 27.0 | 0.0 | 139 | 4.4 | 97 |
| 2026-08-16 13:30:33 | 27.4 | 0.1 | 139 | 3.3 | 95 |
| 2026-08-16 12:30:33 | 30.0 | 0.0 | 139 | 1.8 | 83 |
| 2026-08-16 11:30:29 | 30.1 | 0.1 | 139 | 4.7 | 82 |
| 2026-08-16 10:30:31 | 30.5 | 0.2 | 138 | 9.2 | 78 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 7 day(s)</summary>

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

**2026-08-11**
![2026-08-11 trend](data/chart-history/2026-08-11.png)

**2026-08-10**
![2026-08-10 trend](data/chart-history/2026-08-10.png)

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
