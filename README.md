# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-19 00:30:32 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 23.9 °C |
| 💧 Humidity | 94 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 1.3 km/h |
| 🧭 Wind Direction | 196° |
| 🔵 Pressure | 985.5 hPa |
| 🌫️ AQI (US) | 147 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 98.5 µg/m³ |
| PM10 | 109.2 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-19 00:30:32 | 23.9 | 0.0 | 147 | 1.3 | 94 |
| 2026-09-18 23:30:32 | 24.1 | 0.0 | 143 | 0.4 | 93 |
| 2026-09-18 22:30:30 | 24.2 | 0.0 | 140 | 2.2 | 93 |
| 2026-09-18 21:30:30 | 24.4 | 0.0 | 150 | 3.7 | 92 |
| 2026-09-18 20:30:33 | 24.8 | 0.0 | 149 | 3.7 | 91 |
| 2026-09-18 19:30:33 | 24.5 | 0.0 | 148 | 4.6 | 92 |
| 2026-09-18 18:30:32 | 24.8 | 0.0 | 147 | 4.3 | 92 |
| 2026-09-18 17:30:28 | 25.2 | 0.0 | 146 | 4.2 | 91 |
| 2026-09-18 16:30:35 | 25.7 | 0.0 | 145 | 3.8 | 88 |
| 2026-09-18 15:30:33 | 26.3 | 0.0 | 145 | 3.2 | 86 |
| 2026-09-18 14:30:29 | 26.8 | 0.0 | 145 | 4.8 | 84 |
| 2026-09-18 13:30:34 | 27.8 | 0.0 | 145 | 5.5 | 80 |
| 2026-09-18 12:30:29 | 29.1 | 0.0 | 145 | 4.2 | 77 |
| 2026-09-18 11:30:32 | 30.6 | 0.0 | 144 | 6.9 | 67 |
| 2026-09-18 10:30:37 | 31.5 | 0.0 | 144 | 8.5 | 59 |
| 2026-09-18 09:30:30 | 31.9 | 0.0 | 142 | 8.4 | 58 |
| 2026-09-18 08:30:28 | 32.0 | 0.0 | 142 | 9.5 | 58 |
| 2026-09-18 07:30:36 | 31.8 | 0.0 | 142 | 10.3 | 60 |
| 2026-09-18 06:30:29 | 30.8 | 0.0 | 142 | 11.7 | 64 |
| 2026-09-18 05:30:29 | 29.9 | 0.0 | 142 | 12.3 | 69 |
| 2026-09-18 04:30:30 | 28.8 | 0.0 | 143 | 12.3 | 76 |
| 2026-09-18 03:30:28 | 27.6 | 0.0 | 145 | 12.1 | 81 |
| 2026-09-18 02:30:43 | 26.2 | 0.0 | 146 | 10.8 | 86 |
| 2026-09-18 00:30:35 | 24.1 | 0.0 | 149 | 7.7 | 93 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 43 day(s)</summary>

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
