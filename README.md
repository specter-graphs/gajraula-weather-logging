# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-21 18:30:33 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 26.6 °C |
| 💧 Humidity | 86 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 0.7 km/h |
| 🧭 Wind Direction | 104° |
| 🔵 Pressure | 985.2 hPa |
| 🌫️ AQI (US) | 142 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 77.3 µg/m³ |
| PM10 | 85.7 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-21 18:30:33 | 26.6 | 0.0 | 142 | 0.7 | 86 |
| 2026-09-21 17:30:33 | 27.2 | 0.0 | 142 | 0.4 | 83 |
| 2026-09-21 16:30:34 | 27.5 | 0.0 | 142 | 0.7 | 82 |
| 2026-09-21 15:30:35 | 27.8 | 0.0 | 143 | 2.1 | 81 |
| 2026-09-21 14:30:31 | 28.3 | 0.0 | 144 | 2.9 | 78 |
| 2026-09-21 13:30:31 | 28.8 | 0.0 | 145 | 3.6 | 77 |
| 2026-09-21 12:30:31 | 29.8 | 0.0 | 147 | 3.8 | 75 |
| 2026-09-21 11:30:28 | 31.1 | 0.0 | 148 | 5.4 | 66 |
| 2026-09-21 10:30:31 | 31.9 | 0.0 | 152 | 7.0 | 58 |
| 2026-09-21 09:30:28 | 32.3 | 0.0 | 152 | 6.0 | 55 |
| 2026-09-21 08:30:29 | 32.5 | 0.0 | 152 | 4.7 | 55 |
| 2026-09-21 07:30:30 | 32.4 | 0.0 | 153 | 4.1 | 55 |
| 2026-09-21 06:31:36 | 32.0 | 0.0 | 154 | 5.7 | 55 |
| 2026-09-21 05:31:04 | 31.4 | 0.0 | 154 | 5.6 | 58 |
| 2026-09-21 04:30:30 | 30.4 | 0.0 | 155 | 4.9 | 66 |
| 2026-09-21 03:30:31 | 29.0 | 0.0 | 155 | 3.8 | 75 |
| 2026-09-21 02:30:33 | 27.1 | 0.0 | 155 | 3.3 | 84 |
| 2026-09-21 01:30:27 | 25.2 | 0.0 | 155 | 3.3 | 90 |
| 2026-09-21 00:30:29 | 24.4 | 0.0 | 155 | 3.8 | 92 |
| 2026-09-20 23:30:31 | 24.4 | 0.0 | 155 | 2.3 | 89 |
| 2026-09-20 22:30:27 | 24.5 | 0.0 | 155 | 4.1 | 88 |
| 2026-09-20 21:30:34 | 24.7 | 0.0 | 156 | 4.4 | 87 |
| 2026-09-20 20:30:36 | 25.1 | 0.0 | 156 | 4.2 | 87 |
| 2026-09-20 19:30:28 | 25.5 | 0.0 | 155 | 4.2 | 86 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 46 day(s)</summary>

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
