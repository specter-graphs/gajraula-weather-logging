# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-03 13:30:38 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 28.3 °C |
| 💧 Humidity | 86 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 4.0 km/h |
| 🧭 Wind Direction | 150° |
| 🔵 Pressure | 978.8 hPa |
| 🌫️ AQI (US) | 135 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 32.7 µg/m³ |
| PM10 | 33.5 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-03 13:30:38 | 28.3 | 0.0 | 135 | 4.0 | 86 |
| 2026-09-03 12:30:38 | 29.2 | 0.0 | 123 | 3.9 | 81 |
| 2026-09-03 11:30:35 | 29.0 | 0.1 | 104 | 5.1 | 87 |
| 2026-09-03 10:30:34 | 30.2 | 0.0 | 100 | 5.9 | 79 |
| 2026-09-03 09:30:36 | 31.2 | 0.0 | 102 | 6.3 | 73 |
| 2026-09-03 07:30:32 | 30.5 | 0.0 | 100 | 4.4 | 76 |
| 2026-09-03 06:30:33 | 30.5 | 0.0 | 99 | 6.0 | 75 |
| 2026-09-03 05:30:29 | 29.6 | 0.0 | 98 | 6.7 | 77 |
| 2026-09-03 03:30:33 | 28.1 | 0.0 | 96 | 6.0 | 84 |
| 2026-09-03 01:30:42 | 26.0 | 0.0 | 94 | 5.5 | 93 |
| 2026-09-03 00:30:33 | 25.5 | 0.0 | 93 | 5.7 | 94 |
| 2026-09-02 23:30:32 | 25.6 | 0.0 | 92 | 5.3 | 93 |
| 2026-09-02 21:30:31 | 25.8 | 0.0 | 75 | 4.5 | 93 |
| 2026-09-02 19:30:32 | 25.9 | 0.0 | 74 | 4.7 | 93 |
| 2026-09-02 18:30:31 | 26.0 | 0.0 | 74 | 4.5 | 94 |
| 2026-09-02 17:30:34 | 25.9 | 0.0 | 73 | 5.1 | 95 |
| 2026-09-02 16:30:33 | 26.0 | 0.0 | 72 | 5.6 | 94 |
| 2026-09-02 15:30:45 | 26.2 | 0.0 | 72 | 6.2 | 93 |
| 2026-09-02 14:30:30 | 26.4 | 0.0 | 72 | 6.7 | 92 |
| 2026-09-02 13:30:36 | 26.8 | 0.0 | 72 | 7.1 | 90 |
| 2026-09-02 11:30:33 | 28.2 | 0.0 | 73 | 9.6 | 84 |
| 2026-09-02 10:30:39 | 28.4 | 0.0 | 76 | 10.3 | 84 |
| 2026-09-02 09:30:31 | 27.9 | 0.0 | 79 | 10.8 | 86 |
| 2026-09-02 08:30:35 | 28.2 | 0.0 | 82 | 12.4 | 82 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 27 day(s)</summary>

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
