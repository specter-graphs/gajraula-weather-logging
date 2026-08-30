# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-30 05:30:31 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 31.8 °C |
| 💧 Humidity | 70 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 6.1 km/h |
| 🧭 Wind Direction | 267° |
| 🔵 Pressure | 979.3 hPa |
| 🌫️ AQI (US) | 179 — Unhealthy 🔴 |
| PM2.5 | 73.8 µg/m³ |
| PM10 | 180.2 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-30 05:30:31 | 31.8 | 0.0 | 179 | 6.1 | 70 |
| 2026-08-30 04:30:36 | 31.0 | 0.0 | 179 | 5.8 | 73 |
| 2026-08-30 03:30:34 | 30.0 | 0.0 | 180 | 3.6 | 78 |
| 2026-08-30 02:30:30 | 28.8 | 0.0 | 181 | 3.2 | 85 |
| 2026-08-30 01:30:27 | 27.4 | 0.0 | 181 | 4.8 | 94 |
| 2026-08-30 00:30:34 | 26.7 | 0.0 | 182 | 5.4 | 97 |
| 2026-08-29 23:30:31 | 26.5 | 0.0 | 183 | 6.2 | 97 |
| 2026-08-29 22:30:28 | 26.8 | 0.0 | 184 | 8.1 | 97 |
| 2026-08-29 21:30:38 | 27.1 | 0.0 | 182 | 9.2 | 96 |
| 2026-08-29 20:30:28 | 27.3 | 0.0 | 184 | 8.1 | 94 |
| 2026-08-29 19:30:28 | 27.6 | 0.0 | 185 | 4.4 | 90 |
| 2026-08-29 18:30:30 | 28.0 | 0.0 | 186 | 1.8 | 90 |
| 2026-08-29 17:30:34 | 28.4 | 0.0 | 186 | 1.5 | 88 |
| 2026-08-29 16:30:31 | 29.1 | 0.0 | 186 | 0.6 | 85 |
| 2026-08-29 15:30:29 | 29.6 | 0.0 | 185 | 1.2 | 83 |
| 2026-08-29 14:30:28 | 29.7 | 0.0 | 184 | 3.8 | 83 |
| 2026-08-29 13:30:31 | 30.1 | 0.0 | 183 | 5.2 | 80 |
| 2026-08-29 12:30:32 | 31.3 | 0.0 | 182 | 6.8 | 75 |
| 2026-08-29 11:30:28 | 32.3 | 0.0 | 181 | 7.6 | 70 |
| 2026-08-29 10:30:30 | 33.1 | 0.0 | 181 | 9.2 | 64 |
| 2026-08-29 09:30:32 | 33.2 | 0.0 | 187 | 11.9 | 63 |
| 2026-08-29 08:30:31 | 33.3 | 0.0 | 186 | 13.0 | 62 |
| 2026-08-29 07:30:30 | 33.3 | 0.0 | 184 | 13.1 | 63 |
| 2026-08-29 06:30:37 | 32.6 | 0.0 | 183 | 10.4 | 65 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 23 day(s)</summary>

**2026-08-29**
![2026-08-29 trend](data/chart-history/2026-08-29.png)

**2026-08-28**
![2026-08-28 trend](data/chart-history/2026-08-28.png)

**2026-08-27**
![2026-08-27 trend](data/chart-history/2026-08-27.png)

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

**2026-08-12**
![2026-08-12 trend](data/chart-history/2026-08-12.png)

**2026-08-11**
![2026-08-11 trend](data/chart-history/2026-08-11.png)

**2026-08-10**
![2026-08-10 trend](data/chart-history/2026-08-10.png)

**2026-08-09**
![2026-08-09 trend](data/chart-history/2026-08-09.png)

**2026-08-08**
![2026-08-08 trend](data/chart-history/2026-08-08.png)

**2026-08-07**
![2026-08-07 trend](data/chart-history/2026-08-07.png)

</details>
<!-- HISTORY-END -->

## 📁 Repo structure

```
weather-logger/
├── .github/workflows/update-weather.yml
├── data/weather_log.csv
├── data/day_chart.png
├── data/chart-history/        # every day, unlimited, e.g. 2026-08-08.png
├── scripts/fetch_weather.py
├── scripts/update_readme.py
├── scripts/generate_chart.py
├── scripts/backfill_chart_history.py
├── README.md
└── requirements.txt
```
