# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-27 08:30:34 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 29.9 °C |
| 💧 Humidity | 81 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 3.8 km/h |
| 🧭 Wind Direction | 245° |
| 🔵 Pressure | 976.7 hPa |
| 🌫️ AQI (US) | 149 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 32.7 µg/m³ |
| PM10 | 40.4 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-27 08:30:34 | 29.9 | 0.0 | 149 | 3.8 | 81 |
| 2026-08-27 07:30:29 | 30.7 | 0.0 | 149 | 4.6 | 78 |
| 2026-08-27 06:30:30 | 30.0 | 0.0 | 149 | 4.6 | 80 |
| 2026-08-27 05:30:29 | 28.8 | 0.1 | 149 | 6.9 | 84 |
| 2026-08-27 04:30:31 | 28.1 | 0.1 | 149 | 10.3 | 85 |
| 2026-08-27 03:30:29 | 27.9 | 0.1 | 149 | 9.9 | 87 |
| 2026-08-27 02:30:34 | 27.0 | 0.1 | 150 | 7.8 | 93 |
| 2026-08-27 01:30:30 | 26.3 | 0.1 | 150 | 9.6 | 97 |
| 2026-08-27 00:30:29 | 26.1 | 0.0 | 150 | 9.9 | 98 |
| 2026-08-26 23:30:32 | 25.1 | 0.4 | 150 | 8.3 | 99 |
| 2026-08-26 22:30:29 | 25.4 | 0.2 | 150 | 5.1 | 97 |
| 2026-08-26 21:30:33 | 26.3 | 0.0 | 138 | 0.6 | 97 |
| 2026-08-26 20:30:33 | 26.7 | 0.0 | 136 | 4.4 | 97 |
| 2026-08-26 19:30:39 | 26.8 | 0.0 | 133 | 4.0 | 97 |
| 2026-08-26 18:30:32 | 27.7 | 0.0 | 130 | 4.0 | 93 |
| 2026-08-26 17:30:42 | 27.9 | 0.0 | 130 | 3.4 | 93 |
| 2026-08-26 16:30:38 | 28.2 | 0.0 | 137 | 3.5 | 91 |
| 2026-08-26 14:30:39 | 29.5 | 0.0 | 148 | 2.7 | 85 |
| 2026-08-26 13:30:34 | 30.0 | 0.0 | 148 | 2.9 | 84 |
| 2026-08-26 12:30:32 | 30.7 | 0.0 | 142 | 5.1 | 80 |
| 2026-08-26 11:30:33 | 31.1 | 0.0 | 130 | 6.4 | 73 |
| 2026-08-26 10:30:33 | 31.4 | 0.0 | 120 | 5.4 | 70 |
| 2026-08-26 09:30:30 | 31.4 | 0.0 | 130 | 4.2 | 70 |
| 2026-08-26 08:30:43 | 31.2 | 0.0 | 130 | 3.9 | 72 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 7 day(s)</summary>

**2026-08-26**
![2026-08-26 trend](data/chart-history/2026-08-26.png)

**2026-08-25**
![2026-08-25 trend](data/chart-history/2026-08-25.png)

**2026-08-24**
![2026-08-24 trend](data/chart-history/2026-08-24.png)

**2026-08-23**
![2026-08-23 trend](data/chart-history/2026-08-23.png)

**2026-08-22**
![2026-08-22 trend](data/chart-history/2026-08-22.png)

**2026-08-21**
![2026-08-21 trend](data/chart-history/2026-08-21.png)

**2026-08-20**
![2026-08-20 trend](data/chart-history/2026-08-20.png)

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
