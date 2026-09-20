# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-20 23:30:31 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 24.4 °C |
| 💧 Humidity | 89 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 2.3 km/h |
| 🧭 Wind Direction | 32° |
| 🔵 Pressure | 986.6 hPa |
| 🌫️ AQI (US) | 155 — Unhealthy 🔴 |
| PM2.5 | 72.6 µg/m³ |
| PM10 | 86.4 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-20 23:30:31 | 24.4 | 0.0 | 155 | 2.3 | 89 |
| 2026-09-20 22:30:27 | 24.5 | 0.0 | 155 | 4.1 | 88 |
| 2026-09-20 21:30:34 | 24.7 | 0.0 | 156 | 4.4 | 87 |
| 2026-09-20 20:30:36 | 25.1 | 0.0 | 156 | 4.2 | 87 |
| 2026-09-20 19:30:28 | 25.5 | 0.0 | 155 | 4.2 | 86 |
| 2026-09-20 18:30:28 | 25.4 | 0.0 | 155 | 2.9 | 89 |
| 2026-09-20 17:30:30 | 25.8 | 0.0 | 155 | 2.2 | 89 |
| 2026-09-20 16:30:29 | 26.4 | 0.0 | 155 | 0.6 | 87 |
| 2026-09-20 15:30:30 | 26.8 | 0.0 | 156 | 2.0 | 86 |
| 2026-09-20 14:30:32 | 27.3 | 0.0 | 156 | 3.9 | 82 |
| 2026-09-20 13:30:29 | 28.1 | 0.0 | 156 | 4.5 | 77 |
| 2026-09-20 12:30:31 | 29.5 | 0.0 | 156 | 2.8 | 76 |
| 2026-09-20 11:31:03 | 31.0 | 0.0 | 156 | 5.0 | 66 |
| 2026-09-20 10:30:29 | 32.0 | 0.0 | 157 | 5.5 | 57 |
| 2026-09-20 09:30:28 | 32.4 | 0.0 | 156 | 3.4 | 53 |
| 2026-09-20 08:30:27 | 32.5 | 0.0 | 156 | 2.3 | 54 |
| 2026-09-20 07:30:32 | 32.3 | 0.0 | 155 | 1.4 | 56 |
| 2026-09-20 06:30:33 | 31.3 | 0.0 | 154 | 4.8 | 65 |
| 2026-09-20 05:30:26 | 30.5 | 0.0 | 154 | 5.0 | 71 |
| 2026-09-20 04:30:30 | 29.4 | 0.0 | 153 | 4.3 | 78 |
| 2026-09-20 03:30:31 | 28.0 | 0.0 | 153 | 3.5 | 84 |
| 2026-09-20 02:30:30 | 26.4 | 0.0 | 153 | 4.2 | 89 |
| 2026-09-20 01:30:27 | 25.0 | 0.0 | 153 | 4.6 | 93 |
| 2026-09-20 00:30:29 | 24.4 | 0.0 | 153 | 4.8 | 94 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 45 day(s)</summary>

**2026-09-20**
![2026-09-20 trend](data/chart-history/2026-09-20.png)

**2026-09-19**
![2026-09-19 trend](data/chart-history/2026-09-19.png)

**2026-09-18**
![2026-09-18 trend](data/chart-history/2026-09-18.png)

**2026-09-17**
![2026-09-17 trend](data/chart-history/2026-09-17.png)

**2026-09-16**
![2026-09-16 trend](data/chart-history/2026-09-16.png)

**2026-09-15**
![2026-09-15 trend](data/chart-history/2026-09-15.png)

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
