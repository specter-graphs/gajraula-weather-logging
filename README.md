# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-09-02 07:30:31 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 29.6 °C |
| 💧 Humidity | 75 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 9.2 km/h |
| 🧭 Wind Direction | 102° |
| 🔵 Pressure | 981.0 hPa |
| 🌫️ AQI (US) | 86 — Moderate 🟡 |
| PM2.5 | 12.7 µg/m³ |
| PM10 | 12.8 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-09-02 07:30:31 | 29.6 | 0.0 | 86 | 9.2 | 75 |
| 2026-09-02 06:30:30 | 27.3 | 0.2 | 91 | 9.2 | 89 |
| 2026-09-02 05:30:35 | 28.8 | 0.0 | 95 | 7.8 | 82 |
| 2026-09-02 04:30:33 | 29.5 | 0.0 | 99 | 4.6 | 80 |
| 2026-09-02 03:30:32 | 28.2 | 0.0 | 104 | 2.3 | 86 |
| 2026-09-02 02:30:31 | 26.9 | 0.0 | 110 | 0.9 | 91 |
| 2026-09-02 01:30:31 | 26.1 | 0.0 | 116 | 1.3 | 95 |
| 2026-09-01 23:30:34 | 25.6 | 0.0 | 126 | 4.3 | 96 |
| 2026-09-01 22:30:30 | 25.7 | 0.0 | 129 | 4.3 | 96 |
| 2026-09-01 21:30:33 | 25.9 | 0.0 | 133 | 5.1 | 95 |
| 2026-09-01 20:30:31 | 26.2 | 0.0 | 140 | 5.8 | 93 |
| 2026-09-01 19:30:37 | 26.4 | 0.0 | 148 | 5.7 | 93 |
| 2026-09-01 18:30:35 | 26.3 | 0.0 | 152 | 6.9 | 93 |
| 2026-09-01 17:30:35 | 26.4 | 0.0 | 156 | 6.3 | 93 |
| 2026-09-01 16:30:36 | 26.4 | 0.0 | 159 | 6.5 | 93 |
| 2026-09-01 15:30:35 | 26.5 | 0.0 | 163 | 7.0 | 93 |
| 2026-09-01 14:30:30 | 26.8 | 0.0 | 165 | 6.4 | 91 |
| 2026-09-01 13:30:36 | 27.1 | 0.0 | 168 | 6.6 | 89 |
| 2026-09-01 11:30:32 | 28.8 | 0.0 | 173 | 7.8 | 81 |
| 2026-09-01 10:30:34 | 29.7 | 0.0 | 167 | 5.7 | 77 |
| 2026-09-01 09:30:29 | 29.4 | 0.0 | 169 | 4.4 | 80 |
| 2026-09-01 08:30:29 | 28.4 | 0.1 | 171 | 5.5 | 86 |
| 2026-09-01 07:30:31 | 26.8 | 0.4 | 172 | 7.8 | 94 |
| 2026-09-01 06:30:31 | 29.5 | 0.0 | 173 | 7.1 | 78 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 26 day(s)</summary>

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
