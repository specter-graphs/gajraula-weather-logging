# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-24 17:30:34 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 27.6 °C |
| 💧 Humidity | 91 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 7.1 km/h |
| 🧭 Wind Direction | 139° |
| 🔵 Pressure | 980.0 hPa |
| 🌫️ AQI (US) | 164 — Unhealthy 🔴 |
| PM2.5 | 85.9 µg/m³ |
| PM10 | 93.6 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-24 17:30:34 | 27.6 | 0.0 | 164 | 7.1 | 91 |
| 2026-08-24 16:30:33 | 27.8 | 0.0 | 164 | 5.1 | 90 |
| 2026-08-24 15:30:32 | 28.1 | 0.0 | 164 | 1.8 | 89 |
| 2026-08-24 14:30:32 | 28.5 | 0.0 | 164 | 4.3 | 86 |
| 2026-08-24 13:30:34 | 29.1 | 0.0 | 164 | 6.7 | 83 |
| 2026-08-24 12:30:31 | 29.2 | 0.0 | 163 | 6.8 | 84 |
| 2026-08-24 11:30:32 | 29.7 | 0.0 | 163 | 4.5 | 83 |
| 2026-08-24 10:30:35 | 31.3 | 0.1 | 162 | 5.4 | 75 |
| 2026-08-24 09:30:31 | 32.3 | 0.0 | 164 | 3.7 | 71 |
| 2026-08-24 08:30:28 | 32.0 | 0.0 | 163 | 3.6 | 73 |
| 2026-08-24 07:30:31 | 31.5 | 0.0 | 162 | 4.1 | 76 |
| 2026-08-24 06:30:31 | 30.9 | 0.0 | 162 | 2.4 | 78 |
| 2026-08-24 05:30:34 | 30.5 | 0.0 | 161 | 3.0 | 77 |
| 2026-08-24 04:30:32 | 29.8 | 0.0 | 160 | 2.2 | 79 |
| 2026-08-24 03:30:30 | 28.7 | 0.0 | 158 | 2.7 | 83 |
| 2026-08-24 02:30:30 | 27.3 | 0.0 | 156 | 2.9 | 90 |
| 2026-08-24 01:30:35 | 26.2 | 0.0 | 153 | 2.7 | 95 |
| 2026-08-24 00:30:32 | 25.8 | 0.0 | 147 | 2.6 | 97 |
| 2026-08-23 23:30:31 | 26.1 | 0.0 | 141 | 4.6 | 98 |
| 2026-08-23 22:30:30 | 26.1 | 0.0 | 135 | 5.0 | 97 |
| 2026-08-23 21:30:31 | 26.0 | 0.1 | 92 | 6.4 | 97 |
| 2026-08-23 20:30:33 | 26.1 | 0.1 | 93 | 1.6 | 98 |
| 2026-08-23 19:30:30 | 26.2 | 0.1 | 94 | 0.7 | 97 |
| 2026-08-23 18:30:29 | 26.9 | 0.0 | 95 | 5.4 | 99 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

The last 7 days of full-day trend charts, newest first.

<!-- HISTORY-START -->
<details><summary>Last 7 day(s)</summary>

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

**2026-08-18**
![2026-08-18 trend](data/chart-history/2026-08-18.png)

**2026-08-17**
![2026-08-17 trend](data/chart-history/2026-08-17.png)

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
