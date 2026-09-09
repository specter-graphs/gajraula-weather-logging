# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-09 22:30:29 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 24.4 °C |
| 💧 Humidity | 93 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 5.9 km/h |
| 🧭 Wind Direction | 102° |
| 🔵 Pressure | 981.9 hPa |
| 🌫️ AQI (US) | 152 — Unhealthy 🔴 |
| PM2.5 | 100.4 µg/m³ |
| PM10 | 261.7 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-09 22:30:29 | 24.4 | 0.0 | 152 | 5.9 | 93 |
| 2026-09-09 21:30:32 | 24.5 | 0.0 | 151 | 7.0 | 92 |
| 2026-09-09 20:30:30 | 24.5 | 0.0 | 148 | 9.6 | 92 |
| 2026-09-09 19:30:32 | 26.1 | 0.0 | 143 | 9.4 | 87 |
| 2026-09-09 18:30:33 | 27.2 | 0.0 | 139 | 2.7 | 81 |
| 2026-09-09 17:30:33 | 27.5 | 0.0 | 136 | 6.7 | 80 |
| 2026-09-09 16:30:36 | 27.8 | 0.0 | 133 | 6.1 | 80 |
| 2026-09-09 15:30:43 | 28.1 | 0.0 | 131 | 6.5 | 80 |
| 2026-09-09 14:30:31 | 28.5 | 0.0 | 141 | 7.4 | 80 |
| 2026-09-09 13:30:35 | 29.1 | 0.0 | 149 | 5.9 | 80 |
| 2026-09-09 12:30:36 | 30.3 | 0.0 | 145 | 6.8 | 77 |
| 2026-09-09 11:30:29 | 31.3 | 0.0 | 132 | 8.4 | 72 |
| 2026-09-09 10:30:34 | 31.4 | 0.1 | 127 | 10.1 | 70 |
| 2026-09-09 09:30:30 | 31.9 | 0.1 | 135 | 13.7 | 67 |
| 2026-09-09 08:30:36 | 32.6 | 0.0 | 135 | 15.6 | 63 |
| 2026-09-09 07:30:31 | 32.6 | 0.0 | 135 | 15.5 | 65 |
| 2026-09-09 06:30:33 | 31.9 | 0.0 | 136 | 12.3 | 68 |
| 2026-09-09 05:30:29 | 31.3 | 0.0 | 137 | 10.7 | 71 |
| 2026-09-09 04:30:31 | 30.2 | 0.0 | 138 | 10.1 | 76 |
| 2026-09-09 03:30:29 | 29.0 | 0.0 | 139 | 9.9 | 81 |
| 2026-09-09 02:30:28 | 27.7 | 0.0 | 141 | 7.9 | 86 |
| 2026-09-09 01:30:28 | 26.2 | 0.0 | 142 | 6.9 | 89 |
| 2026-09-09 00:30:33 | 25.6 | 0.0 | 143 | 6.2 | 90 |
| 2026-09-08 23:30:29 | 25.3 | 0.0 | 145 | 5.7 | 89 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 34 day(s)</summary>

**2026-09-09**
![2026-09-09 trend](data/chart-history/2026-09-09.png)

**2026-09-08**
![2026-09-08 trend](data/chart-history/2026-09-08.png)

**2026-09-07**
![2026-09-07 trend](data/chart-history/2026-09-07.png)

**2026-09-06**
![2026-09-06 trend](data/chart-history/2026-09-06.png)

**2026-09-05**
![2026-09-05 trend](data/chart-history/2026-09-05.png)

**2026-09-04**
![2026-09-04 trend](data/chart-history/2026-09-04.png)

**2026-09-03**
![2026-09-03 trend](data/chart-history/2026-09-03.png)

**2026-09-02**
![2026-09-02 trend](data/chart-history/2026-09-02.png)

**2026-09-01**
![2026-09-01 trend](data/chart-history/2026-09-01.png)

**2026-08-31**
![2026-08-31 trend](data/chart-history/2026-08-31.png)

**2026-08-30**
![2026-08-30 trend](data/chart-history/2026-08-30.png)

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
