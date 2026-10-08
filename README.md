# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-10-08 13:30:32 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 25.4 °C |
| 💧 Humidity | 85 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 3.1 km/h |
| 🧭 Wind Direction | 40° |
| 🔵 Pressure | 987.5 hPa |
| 🌫️ AQI (US) | 153 — Unhealthy 🔴 |
| PM2.5 | 78.2 µg/m³ |
| PM10 | 135.5 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-10-08 13:30:32 | 25.4 | 0.0 | 153 | 3.1 | 85 |
| 2026-10-08 12:30:33 | 26.6 | 0.0 | 154 | 0.7 | 83 |
| 2026-10-08 11:30:32 | 27.8 | 0.0 | 153 | 2.2 | 73 |
| 2026-10-08 10:30:39 | 28.5 | 0.0 | 152 | 6.7 | 64 |
| 2026-10-08 09:30:34 | 29.0 | 0.0 | 145 | 7.8 | 62 |
| 2026-10-08 08:30:31 | 28.7 | 0.0 | 143 | 4.8 | 63 |
| 2026-10-08 07:30:37 | 27.7 | 0.0 | 141 | 2.2 | 67 |
| 2026-10-08 06:30:32 | 27.8 | 0.0 | 139 | 4.1 | 66 |
| 2026-10-08 05:30:30 | 26.6 | 0.0 | 138 | 7.6 | 71 |
| 2026-10-08 04:30:34 | 24.9 | 0.0 | 137 | 9.5 | 75 |
| 2026-10-08 03:30:34 | 23.4 | 0.0 | 137 | 9.3 | 78 |
| 2026-10-08 02:30:50 | 22.0 | 0.0 | 138 | 9.7 | 82 |
| 2026-10-08 01:30:37 | 20.8 | 0.0 | 141 | 10.7 | 89 |
| 2026-10-08 00:30:31 | 20.4 | 0.0 | 145 | 11.2 | 94 |
| 2026-10-07 23:30:35 | 20.4 | 0.0 | 146 | 6.9 | 90 |
| 2026-10-07 22:30:32 | 20.8 | 0.0 | 147 | 9.9 | 88 |
| 2026-10-07 21:30:32 | 21.0 | 0.0 | 118 | 12.3 | 89 |
| 2026-10-07 20:30:33 | 21.3 | 0.0 | 119 | 9.9 | 91 |
| 2026-10-07 19:30:31 | 21.7 | 0.0 | 120 | 9.9 | 92 |
| 2026-10-07 18:30:34 | 22.2 | 0.0 | 121 | 5.1 | 97 |
| 2026-10-07 17:30:46 | 22.2 | 0.0 | 123 | 4.1 | 97 |
| 2026-10-07 16:30:33 | 22.3 | 0.0 | 124 | 5.1 | 96 |
| 2026-10-07 15:30:31 | 22.2 | 0.0 | 125 | 6.9 | 96 |
| 2026-10-07 14:30:36 | 22.7 | 0.3 | 126 | 8.9 | 93 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 62 day(s)</summary>

**2026-10-07**
![2026-10-07 trend](data/chart-history/2026-10-07.png)

**2026-10-06**
![2026-10-06 trend](data/chart-history/2026-10-06.png)

**2026-10-05**
![2026-10-05 trend](data/chart-history/2026-10-05.png)

**2026-10-04**
![2026-10-04 trend](data/chart-history/2026-10-04.png)

**2026-10-03**
![2026-10-03 trend](data/chart-history/2026-10-03.png)

**2026-10-02**
![2026-10-02 trend](data/chart-history/2026-10-02.png)

**2026-10-01**
![2026-10-01 trend](data/chart-history/2026-10-01.png)

**2026-09-30**
![2026-09-30 trend](data/chart-history/2026-09-30.png)

**2026-09-29**
![2026-09-29 trend](data/chart-history/2026-09-29.png)

**2026-09-28**
![2026-09-28 trend](data/chart-history/2026-09-28.png)

**2026-09-27**
![2026-09-27 trend](data/chart-history/2026-09-27.png)

**2026-09-26**
![2026-09-26 trend](data/chart-history/2026-09-26.png)

**2026-09-25**
![2026-09-25 trend](data/chart-history/2026-09-25.png)

**2026-09-24**
![2026-09-24 trend](data/chart-history/2026-09-24.png)

**2026-09-23**
![2026-09-23 trend](data/chart-history/2026-09-23.png)

**2026-09-22**
![2026-09-22 trend](data/chart-history/2026-09-22.png)

**2026-09-21**
![2026-09-21 trend](data/chart-history/2026-09-21.png)

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
