# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-26 12:30:32 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 30.7 °C |
| 💧 Humidity | 80 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 5.1 km/h |
| 🧭 Wind Direction | 293° |
| 🔵 Pressure | 976.3 hPa |
| 🌫️ AQI (US) | 142 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 42.6 µg/m³ |
| PM10 | 45.3 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-26 12:30:32 | 30.7 | 0.0 | 142 | 5.1 | 80 |
| 2026-08-26 11:30:33 | 31.1 | 0.0 | 130 | 6.4 | 73 |
| 2026-08-26 10:30:33 | 31.4 | 0.0 | 120 | 5.4 | 70 |
| 2026-08-26 09:30:30 | 31.4 | 0.0 | 130 | 4.2 | 70 |
| 2026-08-26 08:30:43 | 31.2 | 0.0 | 130 | 3.9 | 72 |
| 2026-08-26 07:30:33 | 30.6 | 0.0 | 130 | 3.6 | 76 |
| 2026-08-26 06:30:33 | 32.4 | 0.0 | 129 | 2.8 | 66 |
| 2026-08-26 05:30:33 | 31.8 | 0.0 | 129 | 2.7 | 70 |
| 2026-08-26 04:30:29 | 31.1 | 0.0 | 128 | 4.6 | 74 |
| 2026-08-26 03:30:33 | 30.1 | 0.0 | 127 | 5.0 | 79 |
| 2026-08-26 02:30:33 | 28.8 | 0.0 | 126 | 4.1 | 86 |
| 2026-08-26 01:30:31 | 27.8 | 0.0 | 126 | 4.3 | 92 |
| 2026-08-26 00:30:31 | 27.4 | 0.0 | 125 | 4.0 | 94 |
| 2026-08-25 23:30:30 | 27.3 | 0.0 | 126 | 4.0 | 94 |
| 2026-08-25 22:30:33 | 27.5 | 0.0 | 129 | 4.8 | 93 |
| 2026-08-25 21:30:31 | 27.6 | 0.0 | 158 | 5.2 | 94 |
| 2026-08-25 20:30:32 | 27.7 | 0.0 | 158 | 5.2 | 95 |
| 2026-08-25 19:30:35 | 27.9 | 0.0 | 157 | 4.6 | 95 |
| 2026-08-25 18:30:39 | 27.6 | 0.0 | 155 | 5.5 | 92 |
| 2026-08-25 17:30:34 | 27.5 | 0.0 | 154 | 6.8 | 91 |
| 2026-08-25 16:30:37 | 27.8 | 0.0 | 153 | 6.9 | 89 |
| 2026-08-25 15:30:35 | 28.4 | 0.0 | 152 | 4.8 | 87 |
| 2026-08-25 14:30:36 | 28.8 | 0.0 | 165 | 2.8 | 85 |
| 2026-08-25 13:30:46 | 29.5 | 0.0 | 168 | 2.9 | 82 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 7 day(s)</summary>

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

**2026-08-19**
![2026-08-19 trend](data/chart-history/2026-08-19.png)

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
