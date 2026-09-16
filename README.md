# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-16 09:31:40 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 31.8 °C |
| 💧 Humidity | 65 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 8.6 km/h |
| 🧭 Wind Direction | 271° |
| 🔵 Pressure | 981.9 hPa |
| 🌫️ AQI (US) | 163 — Unhealthy 🔴 |
| PM2.5 | 48.2 µg/m³ |
| PM10 | 50.2 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-16 09:31:40 | 31.8 | 0.0 | 163 | 8.6 | 65 |
| 2026-09-16 08:30:30 | 31.6 | 0.0 | 163 | 6.3 | 67 |
| 2026-09-16 07:30:33 | 31.0 | 0.0 | 163 | 3.3 | 72 |
| 2026-09-16 06:30:30 | 31.5 | 0.0 | 163 | 3.5 | 68 |
| 2026-09-16 05:30:31 | 30.9 | 0.0 | 162 | 1.1 | 72 |
| 2026-09-16 04:30:32 | 30.0 | 0.0 | 162 | 3.1 | 77 |
| 2026-09-16 03:30:26 | 28.8 | 0.0 | 161 | 4.9 | 85 |
| 2026-09-16 02:30:29 | 27.4 | 0.0 | 160 | 3.8 | 92 |
| 2026-09-16 01:30:29 | 26.0 | 0.0 | 158 | 1.9 | 98 |
| 2026-09-16 00:30:33 | 25.4 | 0.0 | 157 | 1.1 | 100 |
| 2026-09-15 23:30:28 | 25.0 | 0.0 | 155 | 0.6 | 100 |
| 2026-09-15 22:30:33 | 25.1 | 0.0 | 133 | 0.8 | 100 |
| 2026-09-15 21:30:29 | 25.2 | 0.0 | 130 | 1.5 | 99 |
| 2026-09-15 20:30:32 | 25.4 | 0.0 | 128 | 1.6 | 98 |
| 2026-09-15 19:30:35 | 25.8 | 0.0 | 126 | 1.8 | 97 |
| 2026-09-15 18:30:33 | 25.8 | 0.0 | 124 | 5.5 | 91 |
| 2026-09-15 17:30:30 | 26.4 | 0.0 | 123 | 7.1 | 89 |
| 2026-09-15 16:30:34 | 26.9 | 0.0 | 138 | 5.2 | 89 |
| 2026-09-15 15:30:31 | 27.3 | 0.0 | 154 | 3.6 | 89 |
| 2026-09-15 14:30:33 | 27.7 | 0.0 | 162 | 2.8 | 88 |
| 2026-09-15 13:30:37 | 28.3 | 0.0 | 163 | 3.9 | 84 |
| 2026-09-15 12:30:35 | 29.8 | 0.0 | 155 | 3.1 | 74 |
| 2026-09-15 11:30:32 | 30.6 | 0.0 | 137 | 3.4 | 73 |
| 2026-09-15 10:30:30 | 31.2 | 0.0 | 114 | 1.5 | 70 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 40 day(s)</summary>

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
