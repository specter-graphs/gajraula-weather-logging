# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-15 15:30:31 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 27.3 °C |
| 💧 Humidity | 89 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 3.6 km/h |
| 🧭 Wind Direction | 93° |
| 🔵 Pressure | 984.9 hPa |
| 🌫️ AQI (US) | 154 — Unhealthy 🔴 |
| PM2.5 | 49.1 µg/m³ |
| PM10 | 49.9 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-15 15:30:31 | 27.3 | 0.0 | 154 | 3.6 | 89 |
| 2026-09-15 14:30:33 | 27.7 | 0.0 | 162 | 2.8 | 88 |
| 2026-09-15 13:30:37 | 28.3 | 0.0 | 163 | 3.9 | 84 |
| 2026-09-15 12:30:35 | 29.8 | 0.0 | 155 | 3.1 | 74 |
| 2026-09-15 11:30:32 | 30.6 | 0.0 | 137 | 3.4 | 73 |
| 2026-09-15 10:30:30 | 31.2 | 0.0 | 114 | 1.5 | 70 |
| 2026-09-15 09:30:29 | 31.5 | 0.0 | 114 | 1.8 | 69 |
| 2026-09-15 08:30:32 | 31.3 | 0.0 | 112 | 4.0 | 69 |
| 2026-09-15 07:30:40 | 31.1 | 0.0 | 111 | 6.4 | 68 |
| 2026-09-15 06:30:31 | 29.8 | 0.0 | 109 | 5.6 | 75 |
| 2026-09-15 05:30:28 | 29.2 | 0.1 | 107 | 7.0 | 77 |
| 2026-09-15 04:30:28 | 28.3 | 0.0 | 106 | 9.1 | 80 |
| 2026-09-15 03:30:32 | 27.0 | 0.0 | 103 | 9.9 | 86 |
| 2026-09-15 02:30:33 | 25.9 | 0.0 | 101 | 11.1 | 91 |
| 2026-09-15 01:30:31 | 25.2 | 0.0 | 98 | 10.0 | 95 |
| 2026-09-15 00:30:29 | 25.1 | 0.0 | 95 | 8.1 | 96 |
| 2026-09-14 23:30:32 | 25.2 | 0.0 | 93 | 6.0 | 98 |
| 2026-09-14 22:30:31 | 25.3 | 0.0 | 90 | 6.1 | 96 |
| 2026-09-14 21:30:30 | 25.2 | 0.0 | 77 | 6.7 | 96 |
| 2026-09-14 20:30:35 | 25.1 | 0.0 | 76 | 7.7 | 96 |
| 2026-09-14 19:30:32 | 25.0 | 0.1 | 75 | 9.2 | 96 |
| 2026-09-14 18:30:33 | 26.6 | 0.0 | 74 | 9.4 | 90 |
| 2026-09-14 17:30:31 | 26.8 | 0.0 | 74 | 9.1 | 89 |
| 2026-09-14 16:30:32 | 27.1 | 0.0 | 92 | 9.6 | 87 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 39 day(s)</summary>

**2026-09-14**
![2026-09-14 trend](data/chart-history/2026-09-14.png)

**2026-09-13**
![2026-09-13 trend](data/chart-history/2026-09-13.png)

**2026-09-12**
![2026-09-12 trend](data/chart-history/2026-09-12.png)

**2026-09-11**
![2026-09-11 trend](data/chart-history/2026-09-11.png)

**2026-09-10**
![2026-09-10 trend](data/chart-history/2026-09-10.png)

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
