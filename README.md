# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-10-05 09:30:32 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 32.1 °C |
| 💧 Humidity | 57 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 5.0 km/h |
| 🧭 Wind Direction | 224° |
| 🔵 Pressure | 984.3 hPa |
| 🌫️ AQI (US) | 169 — Unhealthy 🔴 |
| PM2.5 | 62.6 µg/m³ |
| PM10 | 163.4 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-10-05 09:30:32 | 32.1 | 0.0 | 169 | 5.0 | 57 |
| 2026-10-05 08:30:32 | 32.2 | 0.0 | 168 | 4.6 | 58 |
| 2026-10-05 07:30:32 | 31.9 | 0.0 | 168 | 4.9 | 59 |
| 2026-10-05 06:30:30 | 31.3 | 0.0 | 169 | 5.1 | 62 |
| 2026-10-05 05:30:30 | 30.6 | 0.0 | 169 | 6.0 | 66 |
| 2026-10-05 04:30:31 | 29.6 | 0.0 | 170 | 6.1 | 72 |
| 2026-10-05 03:30:28 | 28.0 | 0.0 | 170 | 4.8 | 80 |
| 2026-10-05 02:30:28 | 26.1 | 0.0 | 172 | 5.2 | 87 |
| 2026-10-05 01:31:10 | 24.0 | 0.0 | 173 | 5.4 | 93 |
| 2026-10-05 00:30:33 | 23.1 | 0.0 | 174 | 3.8 | 96 |
| 2026-10-04 23:30:33 | 23.2 | 0.0 | 175 | 4.7 | 95 |
| 2026-10-04 22:30:30 | 23.4 | 0.0 | 176 | 4.3 | 94 |
| 2026-10-04 21:30:30 | 23.6 | 0.0 | 181 | 3.6 | 94 |
| 2026-10-04 20:30:31 | 24.0 | 0.0 | 181 | 2.9 | 92 |
| 2026-10-04 19:30:32 | 24.4 | 0.0 | 180 | 3.6 | 90 |
| 2026-10-04 18:30:32 | 24.8 | 0.0 | 180 | 2.2 | 93 |
| 2026-10-04 17:30:33 | 25.2 | 0.0 | 179 | 4.8 | 90 |
| 2026-10-04 16:30:31 | 25.6 | 0.0 | 179 | 3.9 | 86 |
| 2026-10-04 15:30:31 | 26.1 | 0.0 | 179 | 2.6 | 81 |
| 2026-10-04 14:30:31 | 26.5 | 0.0 | 178 | 4.0 | 78 |
| 2026-10-04 13:30:29 | 27.3 | 0.0 | 178 | 5.6 | 74 |
| 2026-10-04 12:30:41 | 28.9 | 0.0 | 178 | 5.6 | 72 |
| 2026-10-04 11:30:32 | 30.7 | 0.0 | 178 | 4.2 | 71 |
| 2026-10-04 10:30:29 | 31.6 | 0.0 | 178 | 7.1 | 62 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 59 day(s)</summary>

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
