# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-10-03 04:31:05 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 29.2 °C |
| 💧 Humidity | 70 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 8.6 km/h |
| 🧭 Wind Direction | 278° |
| 🔵 Pressure | 989.8 hPa |
| 🌫️ AQI (US) | 166 — Unhealthy 🔴 |
| PM2.5 | 90.1 µg/m³ |
| PM10 | 203.0 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-10-03 04:31:05 | 29.2 | 0.0 | 166 | 8.6 | 70 |
| 2026-10-03 03:30:32 | 27.4 | 0.0 | 166 | 7.4 | 78 |
| 2026-10-03 02:30:29 | 25.2 | 0.0 | 165 | 8.5 | 84 |
| 2026-10-03 01:30:29 | 23.4 | 0.0 | 164 | 9.0 | 89 |
| 2026-10-03 00:30:29 | 22.7 | 0.0 | 163 | 7.6 | 92 |
| 2026-10-02 23:30:31 | 22.1 | 0.0 | 163 | 5.3 | 91 |
| 2026-10-02 22:30:29 | 22.7 | 0.0 | 162 | 5.7 | 88 |
| 2026-10-02 21:30:31 | 23.3 | 0.0 | 161 | 5.8 | 85 |
| 2026-10-02 20:30:33 | 23.8 | 0.0 | 161 | 6.2 | 83 |
| 2026-10-02 19:30:33 | 24.3 | 0.0 | 161 | 6.9 | 81 |
| 2026-10-02 18:30:35 | 24.3 | 0.0 | 161 | 6.8 | 86 |
| 2026-10-02 17:30:33 | 24.8 | 0.0 | 162 | 6.8 | 85 |
| 2026-10-02 16:30:33 | 25.2 | 0.0 | 162 | 6.6 | 85 |
| 2026-10-02 15:30:37 | 25.8 | 0.0 | 162 | 6.3 | 83 |
| 2026-10-02 14:30:34 | 26.5 | 0.0 | 162 | 6.7 | 80 |
| 2026-10-02 13:30:36 | 27.1 | 0.0 | 161 | 6.9 | 78 |
| 2026-10-02 12:30:36 | 28.2 | 0.0 | 161 | 6.7 | 75 |
| 2026-10-02 11:30:32 | 29.9 | 0.0 | 161 | 8.2 | 69 |
| 2026-10-02 10:30:32 | 31.1 | 0.0 | 161 | 11.4 | 61 |
| 2026-10-02 09:30:29 | 31.6 | 0.0 | 163 | 13.6 | 57 |
| 2026-10-02 08:30:32 | 31.7 | 0.0 | 162 | 13.8 | 57 |
| 2026-10-02 07:30:35 | 31.4 | 0.0 | 161 | 12.9 | 59 |
| 2026-10-02 06:30:27 | 30.6 | 0.0 | 161 | 11.0 | 61 |
| 2026-10-02 05:31:06 | 29.7 | 0.0 | 160 | 10.1 | 66 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 57 day(s)</summary>

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
