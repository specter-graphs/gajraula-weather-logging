# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-10-06 07:30:30 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 29.0 °C |
| 💧 Humidity | 71 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 12.4 km/h |
| 🧭 Wind Direction | 116° |
| 🔵 Pressure | 988.5 hPa |
| 🌫️ AQI (US) | 155 — Unhealthy 🔴 |
| PM2.5 | 56.3 µg/m³ |
| PM10 | 131.8 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-10-06 07:30:30 | 29.0 | 0.0 | 155 | 12.4 | 71 |
| 2026-10-06 06:30:32 | 28.9 | 0.0 | 155 | 7.1 | 70 |
| 2026-10-06 05:30:29 | 27.6 | 0.0 | 156 | 9.3 | 75 |
| 2026-10-06 04:30:34 | 26.3 | 0.0 | 157 | 11.8 | 79 |
| 2026-10-06 03:30:29 | 25.2 | 0.0 | 158 | 13.0 | 84 |
| 2026-10-06 02:30:28 | 24.0 | 0.0 | 161 | 14.6 | 89 |
| 2026-10-06 01:30:29 | 22.8 | 0.0 | 163 | 14.0 | 94 |
| 2026-10-06 00:30:39 | 22.5 | 0.0 | 166 | 11.9 | 95 |
| 2026-10-05 23:30:34 | 23.8 | 0.0 | 168 | 11.4 | 96 |
| 2026-10-05 22:30:31 | 23.9 | 0.0 | 170 | 11.5 | 94 |
| 2026-10-05 21:30:32 | 24.1 | 0.0 | 173 | 12.4 | 93 |
| 2026-10-05 20:35:39 | 24.6 | 0.0 | 174 | 13.4 | 92 |
| 2026-10-05 18:31:08 | 24.8 | 0.0 | 177 | 8.7 | 91 |
| 2026-10-05 17:30:36 | 25.4 | 0.0 | 177 | 8.8 | 90 |
| 2026-10-05 16:30:34 | 26.2 | 0.0 | 177 | 11.3 | 86 |
| 2026-10-05 15:30:31 | 26.5 | 0.0 | 177 | 6.7 | 83 |
| 2026-10-05 14:30:35 | 27.1 | 0.0 | 176 | 1.2 | 79 |
| 2026-10-05 13:30:39 | 27.6 | 0.0 | 179 | 2.7 | 76 |
| 2026-10-05 12:30:32 | 28.7 | 0.0 | 177 | 6.6 | 80 |
| 2026-10-05 11:30:34 | 30.3 | 0.0 | 174 | 4.9 | 72 |
| 2026-10-05 10:30:30 | 31.5 | 0.0 | 174 | 8.3 | 61 |
| 2026-10-05 09:30:32 | 32.1 | 0.0 | 169 | 5.0 | 57 |
| 2026-10-05 08:30:32 | 32.2 | 0.0 | 168 | 4.6 | 58 |
| 2026-10-05 07:30:32 | 31.9 | 0.0 | 168 | 4.9 | 59 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 60 day(s)</summary>

**2026-10-05**
![2026-10-05 trend](data/chart-history/2026-10-05.png)

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
