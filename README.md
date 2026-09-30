# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-30 00:30:37 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 21.7 °C |
| 💧 Humidity | 93 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 7.3 km/h |
| 🧭 Wind Direction | 277° |
| 🔵 Pressure | 985.5 hPa |
| 🌫️ AQI (US) | 113 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 63.1 µg/m³ |
| PM10 | 146.7 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-30 00:30:37 | 21.7 | 0.0 | 113 | 7.3 | 93 |
| 2026-09-29 23:30:28 | 22.1 | 0.0 | 113 | 7.5 | 90 |
| 2026-09-29 22:30:33 | 22.4 | 0.0 | 114 | 8.1 | 88 |
| 2026-09-29 21:30:32 | 22.7 | 0.0 | 141 | 8.8 | 87 |
| 2026-09-29 20:30:39 | 23.0 | 0.0 | 140 | 9.5 | 85 |
| 2026-09-29 19:30:32 | 23.3 | 0.0 | 141 | 9.7 | 84 |
| 2026-09-29 18:30:33 | 23.7 | 0.0 | 141 | 9.8 | 86 |
| 2026-09-29 17:30:29 | 24.1 | 0.0 | 142 | 9.6 | 85 |
| 2026-09-29 16:30:31 | 24.5 | 0.0 | 145 | 9.4 | 84 |
| 2026-09-29 15:30:36 | 24.9 | 0.0 | 148 | 8.6 | 84 |
| 2026-09-29 14:30:34 | 25.2 | 0.0 | 150 | 7.3 | 83 |
| 2026-09-29 13:30:35 | 25.6 | 0.0 | 151 | 6.6 | 82 |
| 2026-09-29 12:30:35 | 26.6 | 0.0 | 152 | 7.3 | 78 |
| 2026-09-29 11:30:31 | 28.1 | 0.0 | 152 | 9.5 | 71 |
| 2026-09-29 10:30:29 | 29.0 | 0.0 | 151 | 12.0 | 65 |
| 2026-09-29 09:30:28 | 29.4 | 0.0 | 154 | 12.8 | 62 |
| 2026-09-29 08:30:31 | 29.4 | 0.0 | 154 | 12.5 | 62 |
| 2026-09-29 07:30:32 | 29.1 | 0.0 | 153 | 12.2 | 62 |
| 2026-09-29 06:30:32 | 28.6 | 0.0 | 153 | 11.8 | 68 |
| 2026-09-29 05:30:28 | 27.6 | 0.0 | 153 | 11.5 | 71 |
| 2026-09-29 04:30:43 | 26.3 | 0.0 | 152 | 10.3 | 78 |
| 2026-09-29 03:30:29 | 24.5 | 0.0 | 152 | 8.7 | 87 |
| 2026-09-29 02:30:28 | 22.8 | 0.0 | 151 | 8.5 | 93 |
| 2026-09-29 01:30:33 | 21.8 | 0.0 | 149 | 9.3 | 95 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 54 day(s)</summary>

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
