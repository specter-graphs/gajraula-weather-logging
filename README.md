# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-11-11 05:30:29 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 25.1 °C |
| 💧 Humidity | 59 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 3.6 km/h |
| 🧭 Wind Direction | 279° |
| 🔵 Pressure | 991.5 hPa |
| 🌫️ AQI (US) | 168 — Unhealthy 🔴 |
| PM2.5 | 96.2 µg/m³ |
| PM10 | 110.8 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-11-11 05:30:29 | 25.1 | 0.0 | 168 | 3.6 | 59 |
| 2026-11-11 04:30:31 | 22.8 | 0.0 | 166 | 2.4 | 67 |
| 2026-11-11 03:30:36 | 20.1 | 0.0 | 165 | 3.3 | 75 |
| 2026-11-11 02:30:33 | 17.5 | 0.0 | 163 | 6.1 | 83 |
| 2026-11-11 01:30:29 | 15.8 | 0.0 | 162 | 7.2 | 90 |
| 2026-11-11 00:30:37 | 15.4 | 0.0 | 160 | 6.2 | 91 |
| 2026-11-10 23:30:34 | 15.8 | 0.0 | 159 | 6.6 | 92 |
| 2026-11-10 22:30:34 | 16.0 | 0.0 | 158 | 6.4 | 92 |
| 2026-11-10 21:30:34 | 16.2 | 0.0 | 157 | 6.0 | 92 |
| 2026-11-10 20:30:36 | 16.5 | 0.0 | 156 | 6.1 | 92 |
| 2026-11-10 19:30:33 | 16.9 | 0.0 | 155 | 6.2 | 92 |
| 2026-11-10 18:30:38 | 17.6 | 0.0 | 154 | 6.2 | 92 |
| 2026-11-10 17:30:40 | 17.9 | 0.0 | 154 | 5.7 | 92 |
| 2026-11-10 16:30:36 | 18.5 | 0.0 | 154 | 4.8 | 90 |
| 2026-11-10 15:30:33 | 19.4 | 0.0 | 154 | 4.2 | 87 |
| 2026-11-10 14:30:35 | 20.1 | 0.0 | 155 | 4.9 | 85 |
| 2026-11-10 13:30:35 | 20.6 | 0.0 | 155 | 6.0 | 80 |
| 2026-11-10 12:30:34 | 21.9 | 0.0 | 156 | 6.7 | 73 |
| 2026-11-10 11:30:38 | 24.1 | 0.0 | 156 | 6.5 | 65 |
| 2026-11-10 10:30:33 | 26.5 | 0.0 | 157 | 8.6 | 53 |
| 2026-11-10 09:30:36 | 27.6 | 0.0 | 158 | 10.7 | 46 |
| 2026-11-10 08:30:33 | 27.8 | 0.0 | 158 | 10.7 | 46 |
| 2026-11-10 07:30:38 | 27.6 | 0.0 | 158 | 9.9 | 47 |
| 2026-11-10 06:30:31 | 26.9 | 0.0 | 159 | 7.8 | 51 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 96 day(s)</summary>

**2026-11-10**
![2026-11-10 trend](data/chart-history/2026-11-10.png)

**2026-11-09**
![2026-11-09 trend](data/chart-history/2026-11-09.png)

**2026-11-08**
![2026-11-08 trend](data/chart-history/2026-11-08.png)

**2026-11-07**
![2026-11-07 trend](data/chart-history/2026-11-07.png)

**2026-11-06**
![2026-11-06 trend](data/chart-history/2026-11-06.png)

**2026-11-05**
![2026-11-05 trend](data/chart-history/2026-11-05.png)

**2026-11-04**
![2026-11-04 trend](data/chart-history/2026-11-04.png)

**2026-11-03**
![2026-11-03 trend](data/chart-history/2026-11-03.png)

**2026-11-02**
![2026-11-02 trend](data/chart-history/2026-11-02.png)

**2026-11-01**
![2026-11-01 trend](data/chart-history/2026-11-01.png)

**2026-10-31**
![2026-10-31 trend](data/chart-history/2026-10-31.png)

**2026-10-30**
![2026-10-30 trend](data/chart-history/2026-10-30.png)

**2026-10-29**
![2026-10-29 trend](data/chart-history/2026-10-29.png)

**2026-10-28**
![2026-10-28 trend](data/chart-history/2026-10-28.png)

**2026-10-27**
![2026-10-27 trend](data/chart-history/2026-10-27.png)

**2026-10-26**
![2026-10-26 trend](data/chart-history/2026-10-26.png)

**2026-10-25**
![2026-10-25 trend](data/chart-history/2026-10-25.png)

**2026-10-24**
![2026-10-24 trend](data/chart-history/2026-10-24.png)

**2026-10-23**
![2026-10-23 trend](data/chart-history/2026-10-23.png)

**2026-10-22**
![2026-10-22 trend](data/chart-history/2026-10-22.png)

**2026-10-21**
![2026-10-21 trend](data/chart-history/2026-10-21.png)

**2026-10-20**
![2026-10-20 trend](data/chart-history/2026-10-20.png)

**2026-10-19**
![2026-10-19 trend](data/chart-history/2026-10-19.png)

**2026-10-18**
![2026-10-18 trend](data/chart-history/2026-10-18.png)

**2026-10-17**
![2026-10-17 trend](data/chart-history/2026-10-17.png)

**2026-10-16**
![2026-10-16 trend](data/chart-history/2026-10-16.png)

**2026-10-15**
![2026-10-15 trend](data/chart-history/2026-10-15.png)

**2026-10-14**
![2026-10-14 trend](data/chart-history/2026-10-14.png)

**2026-10-13**
![2026-10-13 trend](data/chart-history/2026-10-13.png)

**2026-10-12**
![2026-10-12 trend](data/chart-history/2026-10-12.png)

**2026-10-11**
![2026-10-11 trend](data/chart-history/2026-10-11.png)

**2026-10-10**
![2026-10-10 trend](data/chart-history/2026-10-10.png)

**2026-10-09**
![2026-10-09 trend](data/chart-history/2026-10-09.png)

**2026-10-08**
![2026-10-08 trend](data/chart-history/2026-10-08.png)

**2026-10-07**
![2026-10-07 trend](data/chart-history/2026-10-07.png)

**2026-10-06**
![2026-10-06 trend](data/chart-history/2026-10-06.png)

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
