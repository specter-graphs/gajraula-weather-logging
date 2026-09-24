# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-24 12:30:36 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 28.8 °C |
| 💧 Humidity | 75 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 6.5 km/h |
| 🧭 Wind Direction | 113° |
| 🔵 Pressure | 981.5 hPa |
| 🌫️ AQI (US) | 110 — Unhealthy for Sensitive Groups 🟠 |
| PM2.5 | 19.7 µg/m³ |
| PM10 | 19.8 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-24 12:30:36 | 28.8 | 0.0 | 110 | 6.5 | 75 |
| 2026-09-24 11:30:34 | 30.1 | 0.0 | 105 | 4.6 | 67 |
| 2026-09-24 10:30:32 | 30.9 | 0.0 | 107 | 4.7 | 62 |
| 2026-09-24 09:30:31 | 30.9 | 0.0 | 112 | 6.1 | 62 |
| 2026-09-24 08:30:29 | 30.7 | 0.0 | 114 | 7.9 | 64 |
| 2026-09-24 07:30:29 | 30.5 | 0.0 | 117 | 7.3 | 67 |
| 2026-09-24 06:30:32 | 30.2 | 0.0 | 121 | 9.2 | 66 |
| 2026-09-24 05:30:29 | 29.2 | 0.0 | 125 | 9.0 | 71 |
| 2026-09-24 04:30:28 | 28.0 | 0.0 | 130 | 8.3 | 77 |
| 2026-09-24 03:30:30 | 26.6 | 0.0 | 136 | 8.0 | 81 |
| 2026-09-24 02:30:31 | 25.2 | 0.0 | 143 | 8.3 | 86 |
| 2026-09-24 01:30:31 | 24.2 | 0.0 | 150 | 9.8 | 91 |
| 2026-09-24 00:30:30 | 24.1 | 0.0 | 152 | 9.8 | 91 |
| 2026-09-23 23:30:31 | 24.7 | 0.0 | 155 | 11.8 | 93 |
| 2026-09-23 22:30:30 | 25.3 | 0.0 | 159 | 12.8 | 91 |
| 2026-09-23 21:30:36 | 25.7 | 0.0 | 159 | 12.3 | 87 |
| 2026-09-23 20:30:32 | 26.0 | 0.0 | 162 | 10.8 | 85 |
| 2026-09-23 19:30:33 | 26.5 | 0.0 | 164 | 11.2 | 84 |
| 2026-09-23 18:30:31 | 26.7 | 0.0 | 166 | 8.4 | 80 |
| 2026-09-23 17:30:32 | 27.0 | 0.0 | 168 | 6.9 | 79 |
| 2026-09-23 16:30:32 | 27.4 | 0.0 | 169 | 7.5 | 79 |
| 2026-09-23 15:30:31 | 27.6 | 0.0 | 169 | 6.8 | 80 |
| 2026-09-23 14:30:32 | 28.3 | 0.0 | 169 | 3.1 | 77 |
| 2026-09-23 13:30:30 | 29.5 | 0.0 | 170 | 0.6 | 73 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 48 day(s)</summary>

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
