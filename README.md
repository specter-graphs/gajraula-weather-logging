# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-20 10:30:29 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 32.0 °C |
| 💧 Humidity | 57 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 5.5 km/h |
| 🧭 Wind Direction | 324° |
| 🔵 Pressure | 986.4 hPa |
| 🌫️ AQI (US) | 157 — Unhealthy 🔴 |
| PM2.5 | 52.2 µg/m³ |
| PM10 | 73.6 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
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
| 2026-09-19 23:30:29 | 24.0 | 0.0 | 154 | 4.0 | 94 |
| 2026-09-19 22:30:27 | 24.4 | 0.0 | 154 | 4.5 | 92 |
| 2026-09-19 21:30:29 | 24.6 | 0.0 | 154 | 4.9 | 91 |
| 2026-09-19 19:30:27 | 25.1 | 0.0 | 154 | 4.3 | 89 |
| 2026-09-19 18:30:34 | 25.1 | 0.0 | 153 | 1.8 | 94 |
| 2026-09-19 17:30:29 | 25.4 | 0.0 | 152 | 2.8 | 93 |
| 2026-09-19 16:30:38 | 25.7 | 0.0 | 151 | 3.1 | 92 |
| 2026-09-19 15:30:31 | 26.1 | 0.0 | 151 | 2.7 | 91 |
| 2026-09-19 14:30:26 | 26.6 | 0.0 | 158 | 3.6 | 89 |
| 2026-09-19 12:30:29 | 29.1 | 0.0 | 165 | 3.6 | 77 |
| 2026-09-19 11:30:29 | 30.9 | 0.0 | 157 | 3.1 | 63 |
| 2026-09-19 10:30:28 | 31.7 | 0.0 | 150 | 2.5 | 55 |
| 2026-09-19 09:30:31 | 31.8 | 0.0 | 153 | 1.6 | 56 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 44 day(s)</summary>

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
