# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-10-01 07:30:30 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 31.3 °C |
| 💧 Humidity | 60 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 14.4 km/h |
| 🧭 Wind Direction | 292° |
| 🔵 Pressure | 987.6 hPa |
| 🌫️ AQI (US) | 153 — Unhealthy 🔴 |
| PM2.5 | 36.9 µg/m³ |
| PM10 | 61.0 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-10-01 07:30:30 | 31.3 | 0.0 | 153 | 14.4 | 60 |
| 2026-10-01 06:30:32 | 30.2 | 0.0 | 153 | 10.8 | 62 |
| 2026-10-01 05:30:32 | 29.3 | 0.0 | 153 | 9.7 | 66 |
| 2026-10-01 04:30:39 | 27.9 | 0.0 | 152 | 8.7 | 71 |
| 2026-10-01 03:30:32 | 26.0 | 0.0 | 152 | 7.6 | 78 |
| 2026-10-01 02:30:30 | 24.0 | 0.0 | 152 | 8.2 | 85 |
| 2026-10-01 01:30:32 | 22.3 | 0.0 | 152 | 8.0 | 90 |
| 2026-10-01 00:30:35 | 21.7 | 0.0 | 151 | 6.8 | 91 |
| 2026-09-30 23:30:30 | 21.9 | 0.0 | 151 | 6.6 | 88 |
| 2026-09-30 22:30:31 | 22.2 | 0.0 | 152 | 6.8 | 87 |
| 2026-09-30 21:30:35 | 22.7 | 0.0 | 152 | 7.4 | 86 |
| 2026-09-30 20:30:43 | 23.1 | 0.0 | 151 | 8.3 | 84 |
| 2026-09-30 19:30:33 | 23.4 | 0.0 | 151 | 9.0 | 83 |
| 2026-09-30 18:30:35 | 23.8 | 0.0 | 150 | 8.1 | 83 |
| 2026-09-30 17:30:35 | 24.1 | 0.0 | 147 | 8.4 | 83 |
| 2026-09-30 16:30:38 | 24.4 | 0.0 | 144 | 8.0 | 83 |
| 2026-09-30 15:30:32 | 24.7 | 0.0 | 140 | 7.5 | 84 |
| 2026-09-30 14:30:44 | 25.0 | 0.0 | 142 | 6.9 | 85 |
| 2026-09-30 13:30:35 | 25.7 | 0.0 | 150 | 6.5 | 82 |
| 2026-09-30 12:30:33 | 26.7 | 0.0 | 149 | 6.6 | 77 |
| 2026-09-30 11:30:33 | 28.5 | 0.0 | 138 | 8.2 | 70 |
| 2026-09-30 10:30:47 | 29.7 | 0.0 | 129 | 11.5 | 62 |
| 2026-09-30 09:30:31 | 30.2 | 0.0 | 129 | 13.0 | 58 |
| 2026-09-30 08:30:29 | 30.2 | 0.0 | 129 | 13.0 | 58 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 55 day(s)</summary>

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
