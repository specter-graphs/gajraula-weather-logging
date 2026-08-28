# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-08-28 13:30:32 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 30.0 °C |
| 💧 Humidity | 83 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 3.5 km/h |
| 🧭 Wind Direction | 282° |
| 🔵 Pressure | 975.6 hPa |
| 🌫️ AQI (US) | 164 — Unhealthy 🔴 |
| PM2.5 | 72.4 µg/m³ |
| PM10 | 148.1 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-08-28 13:30:32 | 30.0 | 0.0 | 164 | 3.5 | 83 |
| 2026-08-28 12:30:35 | 31.1 | 0.0 | 163 | 5.9 | 77 |
| 2026-08-28 11:30:33 | 32.4 | 0.0 | 163 | 11.3 | 69 |
| 2026-08-28 10:30:37 | 33.0 | 0.0 | 162 | 14.9 | 65 |
| 2026-08-28 09:30:33 | 33.2 | 0.0 | 173 | 16.3 | 64 |
| 2026-08-28 08:30:35 | 33.2 | 0.0 | 172 | 15.7 | 65 |
| 2026-08-28 07:30:30 | 32.9 | 0.0 | 171 | 14.2 | 68 |
| 2026-08-28 06:30:34 | 31.7 | 0.0 | 170 | 5.0 | 82 |
| 2026-08-28 05:30:31 | 31.5 | 0.0 | 169 | 3.6 | 81 |
| 2026-08-28 04:30:30 | 30.8 | 0.0 | 168 | 2.1 | 81 |
| 2026-08-28 03:30:31 | 29.8 | 0.0 | 167 | 1.5 | 83 |
| 2026-08-28 02:30:33 | 28.5 | 0.0 | 164 | 2.1 | 90 |
| 2026-08-28 01:30:33 | 27.5 | 0.0 | 161 | 2.4 | 95 |
| 2026-08-28 00:30:32 | 27.1 | 0.0 | 158 | 2.3 | 95 |
| 2026-08-27 23:30:32 | 26.4 | 0.1 | 155 | 5.2 | 96 |
| 2026-08-27 22:30:35 | 26.9 | 0.0 | 153 | 1.0 | 95 |
| 2026-08-27 21:30:37 | 27.0 | 0.0 | 151 | 2.1 | 95 |
| 2026-08-27 20:30:43 | 27.2 | 0.0 | 151 | 4.2 | 95 |
| 2026-08-27 19:30:33 | 27.3 | 0.0 | 149 | 4.5 | 94 |
| 2026-08-27 18:30:34 | 27.6 | 0.0 | 148 | 2.4 | 92 |
| 2026-08-27 17:30:34 | 27.7 | 0.0 | 148 | 3.8 | 92 |
| 2026-08-27 16:30:31 | 27.9 | 0.0 | 148 | 4.1 | 92 |
| 2026-08-27 15:30:35 | 28.0 | 0.0 | 146 | 5.3 | 91 |
| 2026-08-27 14:30:32 | 28.2 | 0.0 | 145 | 5.5 | 89 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 21 day(s)</summary>

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
