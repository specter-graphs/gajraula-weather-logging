# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-31 20:30:30 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 27.0 °C |
| 💧 Humidity | 98 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 6.8 km/h |
| 🧭 Wind Direction | 93° |
| 🔵 Pressure | 978.3 hPa |
| 🌫️ AQI (US) | 172 — Unhealthy 🔴 |
| PM2.5 | 71.7 µg/m³ |
| PM10 | 135.5 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-31 20:30:30 | 27.0 | 0.0 | 172 | 6.8 | 98 |
| 2026-08-31 19:30:35 | 27.0 | 0.0 | 172 | 4.9 | 98 |
| 2026-08-31 18:30:32 | 27.2 | 0.0 | 172 | 3.4 | 95 |
| 2026-08-31 17:30:32 | 27.2 | 0.0 | 172 | 3.9 | 95 |
| 2026-08-31 16:30:33 | 27.3 | 0.0 | 171 | 4.0 | 95 |
| 2026-08-31 15:30:31 | 27.5 | 0.0 | 169 | 3.9 | 93 |
| 2026-08-31 14:30:33 | 27.9 | 0.0 | 167 | 6.7 | 90 |
| 2026-08-31 13:30:31 | 28.9 | 0.0 | 166 | 6.4 | 86 |
| 2026-08-31 12:30:30 | 30.0 | 0.0 | 165 | 5.8 | 80 |
| 2026-08-31 11:30:31 | 31.3 | 0.0 | 164 | 8.0 | 71 |
| 2026-08-31 10:30:30 | 32.3 | 0.0 | 163 | 8.7 | 66 |
| 2026-08-31 09:30:31 | 32.5 | 0.0 | 162 | 8.9 | 66 |
| 2026-08-31 08:30:35 | 32.5 | 0.0 | 162 | 9.3 | 67 |
| 2026-08-31 07:30:28 | 32.1 | 0.0 | 162 | 8.9 | 68 |
| 2026-08-31 06:30:32 | 30.8 | 0.0 | 162 | 1.8 | 75 |
| 2026-08-31 05:30:35 | 30.4 | 0.0 | 162 | 3.1 | 75 |
| 2026-08-31 04:30:31 | 30.3 | 0.0 | 162 | 6.1 | 74 |
| 2026-08-31 03:30:30 | 29.4 | 0.0 | 163 | 8.0 | 77 |
| 2026-08-31 02:30:30 | 28.5 | 0.0 | 163 | 7.2 | 85 |
| 2026-08-31 01:30:31 | 27.9 | 0.0 | 164 | 6.2 | 93 |
| 2026-08-31 00:30:33 | 27.6 | 0.0 | 165 | 7.0 | 97 |
| 2026-08-30 23:30:29 | 27.1 | 0.1 | 166 | 4.1 | 98 |
| 2026-08-30 22:30:32 | 27.0 | 0.0 | 167 | 4.2 | 98 |
| 2026-08-30 21:30:32 | 27.0 | 0.0 | 167 | 4.6 | 98 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 25 day(s)</summary>

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
