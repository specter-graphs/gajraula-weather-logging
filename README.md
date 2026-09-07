# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-07 17:30:29 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 25.3 °C |
| 💧 Humidity | 93 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 5.8 km/h |
| 🧭 Wind Direction | 189° |
| 🔵 Pressure | 982.3 hPa |
| 🌫️ AQI (US) | 104 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 60.3 µg/m³ |
| PM10 | 61.2 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-07 17:30:29 | 25.3 | 0.0 | 104 | 5.8 | 93 |
| 2026-09-07 16:30:31 | 25.7 | 0.0 | 105 | 6.1 | 91 |
| 2026-09-07 15:30:29 | 26.1 | 0.0 | 105 | 5.3 | 89 |
| 2026-09-07 14:30:30 | 26.6 | 0.0 | 106 | 5.3 | 87 |
| 2026-09-07 13:30:30 | 27.4 | 0.0 | 107 | 4.5 | 86 |
| 2026-09-07 12:30:30 | 27.5 | 0.0 | 109 | 1.8 | 88 |
| 2026-09-07 11:30:31 | 28.2 | 0.0 | 111 | 6.5 | 85 |
| 2026-09-07 10:30:31 | 28.1 | 0.0 | 112 | 9.6 | 86 |
| 2026-09-07 09:30:35 | 28.3 | 0.1 | 117 | 9.7 | 82 |
| 2026-09-07 08:30:36 | 30.3 | 0.0 | 116 | 6.1 | 72 |
| 2026-09-07 07:30:31 | 31.4 | 0.1 | 116 | 8.8 | 67 |
| 2026-09-07 06:30:29 | 26.4 | 0.1 | 115 | 8.9 | 90 |
| 2026-09-07 05:30:28 | 25.5 | 0.5 | 114 | 9.1 | 97 |
| 2026-09-07 04:30:32 | 26.4 | 0.6 | 113 | 7.5 | 91 |
| 2026-09-07 03:30:27 | 26.6 | 0.1 | 111 | 5.7 | 87 |
| 2026-09-07 02:30:29 | 25.5 | 0.0 | 109 | 5.1 | 90 |
| 2026-09-07 01:30:32 | 24.4 | 0.0 | 107 | 6.2 | 95 |
| 2026-09-07 00:30:30 | 23.8 | 0.0 | 104 | 6.9 | 99 |
| 2026-09-06 23:30:29 | 23.9 | 0.2 | 101 | 9.1 | 97 |
| 2026-09-06 22:30:30 | 24.2 | 0.0 | 114 | 6.8 | 96 |
| 2026-09-06 21:30:28 | 24.4 | 0.0 | 109 | 6.9 | 96 |
| 2026-09-06 20:30:30 | 24.6 | 0.0 | 104 | 6.0 | 96 |
| 2026-09-06 19:30:37 | 24.7 | 0.0 | 99 | 4.7 | 95 |
| 2026-09-06 18:30:29 | 25.4 | 0.0 | 95 | 4.7 | 95 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 31 day(s)</summary>

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
