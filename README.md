# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-11-24 20:30:38 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 13.1 °C |
| 💧 Humidity | 92 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 5.4 km/h |
| 🧭 Wind Direction | 300° |
| 🔵 Pressure | 991.9 hPa |
| 🌫️ AQI (US) | 167 — Unhealthy 🔴 |
| PM2.5 | 116.2 µg/m³ |
| PM10 | 116.6 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-11-24 20:30:38 | 13.1 | 0.0 | 167 | 5.4 | 92 |
| 2026-11-24 19:30:37 | 13.7 | 0.0 | 165 | 5.9 | 91 |
| 2026-11-24 18:30:36 | 14.3 | 0.0 | 164 | 2.3 | 92 |
| 2026-11-24 17:30:36 | 15.1 | 0.0 | 163 | 1.3 | 88 |
| 2026-11-24 16:30:46 | 15.9 | 0.0 | 161 | 0.7 | 85 |
| 2026-11-24 15:30:45 | 16.6 | 0.0 | 161 | 0.9 | 82 |
| 2026-11-24 14:30:37 | 17.3 | 0.0 | 160 | 1.5 | 79 |
| 2026-11-24 13:30:43 | 18.1 | 0.0 | 159 | 2.9 | 76 |
| 2026-11-24 12:30:38 | 18.2 | 0.0 | 159 | 5.0 | 74 |
| 2026-11-24 11:30:43 | 20.0 | 0.0 | 159 | 4.4 | 69 |
| 2026-11-24 10:30:39 | 22.2 | 0.0 | 159 | 5.8 | 57 |
| 2026-11-24 09:30:35 | 23.1 | 0.0 | 158 | 7.5 | 49 |
| 2026-11-24 05:30:41 | 20.3 | 0.0 | 160 | 4.4 | 60 |
| 2026-11-24 03:30:34 | 16.3 | 0.0 | 162 | 3.9 | 71 |
| 2026-11-24 01:30:41 | 12.7 | 0.0 | 166 | 7.4 | 82 |
| 2026-11-24 00:30:44 | 13.4 | 0.0 | 167 | 9.2 | 78 |
| 2026-11-23 23:30:35 | 13.7 | 0.0 | 169 | 9.2 | 77 |
| 2026-11-23 21:30:38 | 14.3 | 0.0 | 171 | 9.0 | 75 |
| 2026-11-23 20:30:35 | 14.8 | 0.0 | 172 | 8.9 | 73 |
| 2026-11-23 19:30:37 | 15.2 | 0.0 | 173 | 9.7 | 73 |
| 2026-11-23 18:30:40 | 14.8 | 0.0 | 173 | 8.4 | 82 |
| 2026-11-23 17:30:39 | 15.1 | 0.0 | 174 | 7.2 | 84 |
| 2026-11-23 16:30:40 | 15.6 | 0.0 | 174 | 7.3 | 85 |
| 2026-11-23 15:30:38 | 16.0 | 0.0 | 174 | 6.6 | 85 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 110 day(s)</summary>

**2026-11-24**
![2026-11-24 trend](data/chart-history/2026-11-24.png)

**2026-11-23**
![2026-11-23 trend](data/chart-history/2026-11-23.png)

**2026-11-22**
![2026-11-22 trend](data/chart-history/2026-11-22.png)

**2026-11-21**
![2026-11-21 trend](data/chart-history/2026-11-21.png)

**2026-11-20**
![2026-11-20 trend](data/chart-history/2026-11-20.png)

**2026-11-19**
![2026-11-19 trend](data/chart-history/2026-11-19.png)

**2026-11-18**
![2026-11-18 trend](data/chart-history/2026-11-18.png)

**2026-11-17**
![2026-11-17 trend](data/chart-history/2026-11-17.png)

**2026-11-16**
![2026-11-16 trend](data/chart-history/2026-11-16.png)

**2026-11-15**
![2026-11-15 trend](data/chart-history/2026-11-15.png)

**2026-11-14**
![2026-11-14 trend](data/chart-history/2026-11-14.png)

**2026-11-13**
![2026-11-13 trend](data/chart-history/2026-11-13.png)

**2026-11-12**
![2026-11-12 trend](data/chart-history/2026-11-12.png)

**2026-11-11**
![2026-11-11 trend](data/chart-history/2026-11-11.png)

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
