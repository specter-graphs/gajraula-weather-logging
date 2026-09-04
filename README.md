# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-04 06:30:33 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 29.1 °C |
| 💧 Humidity | 77 % |
| 🌧️ Rain (last hr) | 0.2 mm |
| 💨 Wind Speed | 9.5 km/h |
| 🧭 Wind Direction | 88° |
| 🔵 Pressure | 982.0 hPa |
| 🌫️ AQI (US) | 99 — Moderate 🟡 |
| PM2.5 | 25.6 µg/m³ |
| PM10 | 26.3 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-04 06:30:33 | 29.1 | 0.2 | 99 | 9.5 | 77 |
| 2026-09-04 05:31:04 | 29.5 | 0.1 | 99 | 9.7 | 78 |
| 2026-09-04 04:30:28 | 29.2 | 0.0 | 99 | 7.8 | 82 |
| 2026-09-04 03:30:31 | 28.3 | 0.0 | 99 | 5.9 | 88 |
| 2026-09-04 02:30:30 | 27.2 | 0.0 | 98 | 5.4 | 93 |
| 2026-09-04 01:30:32 | 26.2 | 0.0 | 97 | 3.8 | 96 |
| 2026-09-04 00:30:35 | 25.8 | 0.0 | 95 | 1.5 | 97 |
| 2026-09-03 22:30:35 | 26.3 | 0.0 | 94 | 3.2 | 96 |
| 2026-09-03 21:30:30 | 26.5 | 0.0 | 98 | 2.4 | 95 |
| 2026-09-03 20:30:33 | 26.6 | 0.1 | 97 | 1.7 | 93 |
| 2026-09-03 19:30:31 | 26.6 | 0.1 | 97 | 1.5 | 95 |
| 2026-09-03 18:30:41 | 26.5 | 0.0 | 98 | 1.8 | 95 |
| 2026-09-03 17:30:32 | 26.9 | 0.0 | 100 | 0.9 | 93 |
| 2026-09-03 16:30:35 | 27.1 | 0.0 | 104 | 1.5 | 92 |
| 2026-09-03 15:30:33 | 27.3 | 0.0 | 123 | 3.0 | 91 |
| 2026-09-03 14:30:34 | 27.7 | 0.0 | 135 | 4.9 | 88 |
| 2026-09-03 13:30:38 | 28.3 | 0.0 | 135 | 4.0 | 86 |
| 2026-09-03 12:30:38 | 29.2 | 0.0 | 123 | 3.9 | 81 |
| 2026-09-03 11:30:35 | 29.0 | 0.1 | 104 | 5.1 | 87 |
| 2026-09-03 10:30:34 | 30.2 | 0.0 | 100 | 5.9 | 79 |
| 2026-09-03 09:30:36 | 31.2 | 0.0 | 102 | 6.3 | 73 |
| 2026-09-03 07:30:32 | 30.5 | 0.0 | 100 | 4.4 | 76 |
| 2026-09-03 06:30:33 | 30.5 | 0.0 | 99 | 6.0 | 75 |
| 2026-09-03 05:30:29 | 29.6 | 0.0 | 98 | 6.7 | 77 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 28 day(s)</summary>

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
