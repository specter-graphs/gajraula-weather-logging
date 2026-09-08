# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-08 22:30:30 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 25.4 °C |
| 💧 Humidity | 89 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 5.9 km/h |
| 🧭 Wind Direction | 272° |
| 🔵 Pressure | 980.4 hPa |
| 🌫️ AQI (US) | 150 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 62.9 µg/m³ |
| PM10 | 94.8 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-08 22:30:30 | 25.4 | 0.0 | 150 | 5.9 | 89 |
| 2026-09-08 21:30:31 | 25.6 | 0.0 | 151 | 6.0 | 88 |
| 2026-09-08 20:30:32 | 26.0 | 0.0 | 151 | 5.4 | 87 |
| 2026-09-08 19:30:34 | 26.3 | 0.0 | 151 | 6.4 | 87 |
| 2026-09-08 18:30:30 | 26.6 | 0.0 | 152 | 6.7 | 85 |
| 2026-09-08 17:30:33 | 26.9 | 0.0 | 153 | 6.8 | 83 |
| 2026-09-08 16:30:30 | 27.3 | 0.0 | 154 | 7.4 | 81 |
| 2026-09-08 15:30:34 | 27.8 | 0.0 | 154 | 8.5 | 79 |
| 2026-09-08 14:30:34 | 28.2 | 0.0 | 167 | 9.0 | 78 |
| 2026-09-08 13:30:31 | 28.7 | 0.0 | 172 | 7.9 | 77 |
| 2026-09-08 12:30:31 | 29.8 | 0.0 | 168 | 7.6 | 75 |
| 2026-09-08 11:30:33 | 31.1 | 0.0 | 154 | 10.2 | 69 |
| 2026-09-08 10:30:31 | 31.8 | 0.0 | 152 | 13.2 | 63 |
| 2026-09-08 09:30:34 | 32.1 | 0.0 | 154 | 14.2 | 60 |
| 2026-09-08 08:30:32 | 32.1 | 0.0 | 153 | 14.5 | 59 |
| 2026-09-08 07:30:37 | 32.1 | 0.0 | 151 | 13.8 | 59 |
| 2026-09-08 06:30:39 | 31.6 | 0.0 | 150 | 8.8 | 64 |
| 2026-09-08 05:30:35 | 31.2 | 0.0 | 145 | 7.6 | 65 |
| 2026-09-08 04:30:35 | 30.3 | 0.0 | 141 | 6.3 | 71 |
| 2026-09-08 03:30:35 | 28.7 | 0.0 | 137 | 5.3 | 80 |
| 2026-09-08 02:30:28 | 26.8 | 0.0 | 133 | 4.5 | 89 |
| 2026-09-08 01:30:36 | 25.0 | 0.0 | 129 | 4.2 | 94 |
| 2026-09-08 00:30:29 | 24.3 | 0.0 | 125 | 2.5 | 93 |
| 2026-09-07 23:30:27 | 24.3 | 0.0 | 124 | 2.0 | 93 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 33 day(s)</summary>

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
