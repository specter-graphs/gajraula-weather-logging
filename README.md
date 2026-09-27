# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-27 07:30:33 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 22.3 °C |
| 💧 Humidity | 90 % |
| 🌧️ Rain (last hr) | 0.1 mm |
| 💨 Wind Speed | 8.3 km/h |
| 🧭 Wind Direction | 6° |
| 🔵 Pressure | 983.7 hPa |
| 🌫️ AQI (US) | 97 — Moderate 🟡 |
| PM2.5 | 9.0 µg/m³ |
| PM10 | 9.0 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-27 07:30:33 | 22.3 | 0.1 | 97 | 8.3 | 90 |
| 2026-09-27 06:30:31 | 23.2 | 0.1 | 99 | 14.5 | 86 |
| 2026-09-27 05:30:43 | 22.9 | 0.1 | 99 | 14.3 | 90 |
| 2026-09-27 04:30:31 | 22.6 | 0.2 | 98 | 16.1 | 89 |
| 2026-09-27 03:30:30 | 22.2 | 0.1 | 97 | 16.2 | 89 |
| 2026-09-27 02:30:30 | 22.0 | 0.2 | 95 | 14.9 | 90 |
| 2026-09-27 01:30:32 | 21.9 | 0.0 | 93 | 8.5 | 92 |
| 2026-09-27 00:30:29 | 21.7 | 0.2 | 91 | 1.8 | 94 |
| 2026-09-26 23:30:32 | 21.8 | 0.5 | 91 | 2.8 | 91 |
| 2026-09-26 22:30:30 | 21.9 | 0.6 | 92 | 3.9 | 88 |
| 2026-09-26 21:30:30 | 21.6 | 0.6 | 79 | 11.4 | 89 |
| 2026-09-26 20:30:31 | 21.4 | 0.2 | 81 | 14.1 | 91 |
| 2026-09-26 19:30:30 | 21.5 | 0.6 | 83 | 13.1 | 91 |
| 2026-09-26 18:30:33 | 21.6 | 0.5 | 85 | 10.9 | 93 |
| 2026-09-26 17:30:31 | 21.7 | 1.5 | 86 | 12.5 | 90 |
| 2026-09-26 16:30:29 | 21.7 | 2.1 | 87 | 18.6 | 87 |
| 2026-09-26 15:30:31 | 21.7 | 1.6 | 88 | 24.7 | 88 |
| 2026-09-26 14:30:29 | 22.4 | 1.9 | 89 | 19.5 | 91 |
| 2026-09-26 13:30:29 | 22.8 | 1.8 | 90 | 13.5 | 92 |
| 2026-09-26 12:30:32 | 22.9 | 1.3 | 90 | 9.2 | 92 |
| 2026-09-26 11:30:33 | 22.9 | 1.5 | 89 | 18.7 | 93 |
| 2026-09-26 10:30:30 | 23.2 | 1.8 | 88 | 18.9 | 93 |
| 2026-09-26 09:30:28 | 23.4 | 1.6 | 101 | 20.7 | 95 |
| 2026-09-26 08:30:26 | 23.5 | 2.5 | 97 | 16.8 | 95 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 51 day(s)</summary>

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
