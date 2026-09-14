# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-14 06:30:33 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 30.9 °C |
| 💧 Humidity | 74 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 12.6 km/h |
| 🧭 Wind Direction | 114° |
| 🔵 Pressure | 987.7 hPa |
| 🌫️ AQI (US) | 66 — Moderate 🟡 |
| PM2.5 | 17.6 µg/m³ |
| PM10 | 18.3 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-14 06:30:33 | 30.9 | 0.0 | 66 | 12.6 | 74 |
| 2026-09-14 05:30:35 | 30.2 | 0.0 | 66 | 13.4 | 76 |
| 2026-09-14 04:30:33 | 29.3 | 0.1 | 66 | 14.2 | 78 |
| 2026-09-14 03:30:31 | 28.4 | 0.1 | 67 | 15.0 | 82 |
| 2026-09-14 02:30:34 | 27.5 | 0.0 | 67 | 12.3 | 87 |
| 2026-09-14 01:30:34 | 26.5 | 0.0 | 68 | 9.6 | 92 |
| 2026-09-14 00:30:30 | 26.1 | 0.0 | 69 | 9.0 | 94 |
| 2026-09-13 23:30:32 | 24.5 | 0.4 | 70 | 8.9 | 96 |
| 2026-09-13 22:30:33 | 25.1 | 0.0 | 71 | 7.8 | 95 |
| 2026-09-13 21:30:31 | 26.3 | 0.0 | 77 | 11.2 | 91 |
| 2026-09-13 20:31:09 | 26.5 | 0.0 | 77 | 10.8 | 90 |
| 2026-09-13 19:30:35 | 26.8 | 0.0 | 78 | 10.5 | 89 |
| 2026-09-13 18:30:31 | 26.8 | 0.0 | 79 | 9.6 | 92 |
| 2026-09-13 17:30:32 | 26.9 | 0.0 | 80 | 10.0 | 92 |
| 2026-09-13 16:30:30 | 26.9 | 0.0 | 80 | 9.0 | 91 |
| 2026-09-13 15:30:32 | 27.1 | 0.0 | 95 | 8.7 | 90 |
| 2026-09-13 14:30:45 | 27.6 | 0.0 | 106 | 9.4 | 88 |
| 2026-09-13 13:30:33 | 28.0 | 0.0 | 111 | 9.6 | 85 |
| 2026-09-13 12:30:35 | 28.6 | 0.0 | 109 | 9.6 | 82 |
| 2026-09-13 11:30:33 | 29.0 | 0.0 | 100 | 13.0 | 80 |
| 2026-09-13 10:30:31 | 30.3 | 0.0 | 84 | 14.2 | 74 |
| 2026-09-13 09:30:33 | 31.5 | 0.1 | 79 | 11.3 | 67 |
| 2026-09-13 08:30:33 | 31.7 | 0.0 | 79 | 11.9 | 66 |
| 2026-09-13 07:30:35 | 31.8 | 0.0 | 78 | 13.0 | 66 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 38 day(s)</summary>

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
