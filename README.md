# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-20 04:30:29 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 30.6 °C |
| 💧 Humidity | 79 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 4.2 km/h |
| 🧭 Wind Direction | 31° |
| 🔵 Pressure | 980.8 hPa |
| 🌫️ AQI (US) | 123 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 31.7 µg/m³ |
| PM10 | 35.4 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
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
| 2026-08-19 15:30:34 | 27.0 | 0.1 | 141 | 5.8 | 95 |
| 2026-08-19 14:30:31 | 27.1 | 0.0 | 142 | 4.2 | 93 |
| 2026-08-19 13:30:32 | 27.2 | 0.0 | 143 | 3.1 | 94 |
| 2026-08-19 12:30:35 | 28.3 | 0.2 | 144 | 5.0 | 91 |
| 2026-08-19 11:30:36 | 30.8 | 0.0 | 144 | 6.1 | 78 |
| 2026-08-19 10:30:33 | 32.7 | 0.0 | 143 | 4.7 | 69 |
| 2026-08-19 09:32:03 | 32.8 | 0.0 | 152 | 3.3 | 69 |
| 2026-08-19 08:30:33 | 32.7 | 0.0 | 152 | 2.2 | 71 |
| 2026-08-19 07:30:35 | 32.3 | 0.0 | 151 | 1.5 | 73 |
| 2026-08-19 06:30:31 | 31.5 | 0.0 | 151 | 4.2 | 73 |
| 2026-08-19 05:30:52 | 30.1 | 0.0 | 151 | 3.7 | 79 |

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
