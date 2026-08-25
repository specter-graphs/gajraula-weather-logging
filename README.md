# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-25 18:30:39 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 27.6 °C |
| 💧 Humidity | 92 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 5.5 km/h |
| 🧭 Wind Direction | 189° |
| 🔵 Pressure | 980.1 hPa |
| 🌫️ AQI (US) | 155 — Unhealthy 🔴 |
| PM2.5 | 141.1 µg/m³ |
| PM10 | 146.7 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-25 18:30:39 | 27.6 | 0.0 | 155 | 5.5 | 92 |
| 2026-08-25 17:30:34 | 27.5 | 0.0 | 154 | 6.8 | 91 |
| 2026-08-25 16:30:37 | 27.8 | 0.0 | 153 | 6.9 | 89 |
| 2026-08-25 15:30:35 | 28.4 | 0.0 | 152 | 4.8 | 87 |
| 2026-08-25 14:30:36 | 28.8 | 0.0 | 165 | 2.8 | 85 |
| 2026-08-25 13:30:46 | 29.5 | 0.0 | 168 | 2.9 | 82 |
| 2026-08-25 12:30:33 | 30.8 | 0.0 | 161 | 2.3 | 74 |
| 2026-08-25 11:30:30 | 31.3 | 0.0 | 153 | 3.0 | 71 |
| 2026-08-25 10:30:31 | 31.8 | 0.0 | 151 | 2.4 | 68 |
| 2026-08-25 09:30:33 | 32.1 | 0.0 | 151 | 4.1 | 67 |
| 2026-08-25 08:30:32 | 32.0 | 0.0 | 152 | 5.0 | 68 |
| 2026-08-25 07:30:30 | 31.7 | 0.0 | 153 | 2.4 | 71 |
| 2026-08-25 06:30:29 | 31.9 | 0.0 | 154 | 2.8 | 72 |
| 2026-08-25 05:30:33 | 31.2 | 0.0 | 154 | 1.3 | 75 |
| 2026-08-25 04:30:30 | 30.2 | 0.0 | 155 | 1.3 | 81 |
| 2026-08-25 03:30:30 | 28.6 | 0.0 | 157 | 2.7 | 88 |
| 2026-08-25 02:30:30 | 27.5 | 0.0 | 158 | 4.0 | 94 |
| 2026-08-25 01:30:28 | 26.9 | 0.0 | 158 | 4.4 | 97 |
| 2026-08-25 00:30:32 | 26.3 | 0.0 | 159 | 4.0 | 99 |
| 2026-08-24 23:30:30 | 26.4 | 0.0 | 161 | 1.5 | 99 |
| 2026-08-24 22:30:33 | 26.5 | 0.0 | 162 | 0.8 | 98 |
| 2026-08-24 21:30:34 | 26.6 | 0.0 | 163 | 4.0 | 97 |
| 2026-08-24 20:30:36 | 26.7 | 0.0 | 163 | 2.0 | 97 |
| 2026-08-24 19:30:33 | 26.8 | 0.0 | 163 | 2.2 | 96 |

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
