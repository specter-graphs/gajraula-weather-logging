# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-13 06:30:36 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 31.1 °C |
| 💧 Humidity | 74 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 11.4 km/h |
| 🧭 Wind Direction | 84° |
| 🔵 Pressure | 986.9 hPa |
| 🌫️ AQI (US) | 78 — Moderate 🟡 |
| PM2.5 | 20.0 µg/m³ |
| PM10 | 20.8 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-13 06:30:36 | 31.1 | 0.0 | 78 | 11.4 | 74 |
| 2026-09-13 05:30:31 | 30.6 | 0.0 | 78 | 13.0 | 75 |
| 2026-09-13 04:30:37 | 30.4 | 0.0 | 78 | 13.4 | 74 |
| 2026-09-13 03:30:34 | 29.7 | 0.0 | 78 | 10.8 | 79 |
| 2026-09-13 02:30:30 | 28.4 | 0.0 | 78 | 8.2 | 87 |
| 2026-09-13 01:30:30 | 27.0 | 0.0 | 78 | 7.7 | 93 |
| 2026-09-13 00:30:42 | 26.3 | 0.0 | 78 | 8.1 | 94 |
| 2026-09-12 23:30:30 | 26.2 | 0.0 | 78 | 9.1 | 91 |
| 2026-09-12 22:30:29 | 26.3 | 0.0 | 78 | 9.3 | 91 |
| 2026-09-12 21:30:31 | 26.4 | 0.0 | 78 | 9.0 | 92 |
| 2026-09-12 20:30:34 | 26.5 | 0.0 | 78 | 8.3 | 91 |
| 2026-09-12 19:30:33 | 26.8 | 0.0 | 77 | 7.7 | 91 |
| 2026-09-12 18:30:45 | 27.0 | 0.0 | 76 | 8.6 | 93 |
| 2026-09-12 17:30:33 | 27.1 | 0.0 | 75 | 8.3 | 93 |
| 2026-09-12 16:30:32 | 27.3 | 0.0 | 74 | 7.6 | 92 |
| 2026-09-12 15:30:32 | 27.5 | 0.0 | 77 | 6.7 | 91 |
| 2026-09-12 14:30:34 | 27.8 | 0.0 | 87 | 7.3 | 89 |
| 2026-09-12 13:30:36 | 28.2 | 0.0 | 89 | 8.8 | 86 |
| 2026-09-12 12:30:34 | 29.2 | 0.0 | 83 | 9.8 | 82 |
| 2026-09-12 11:30:29 | 31.2 | 0.0 | 70 | 7.6 | 72 |
| 2026-09-12 10:30:31 | 31.8 | 0.0 | 71 | 9.7 | 66 |
| 2026-09-12 09:30:31 | 32.0 | 0.0 | 72 | 11.5 | 65 |
| 2026-09-12 08:30:34 | 32.1 | 0.0 | 72 | 12.5 | 64 |
| 2026-09-12 07:30:36 | 31.9 | 0.0 | 73 | 12.7 | 66 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 37 day(s)</summary>

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
