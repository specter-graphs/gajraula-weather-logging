# 🌦️ Weather & AQI Logger

Automated Weather Logger. Logs Temperature,Humidity,Wind speed, Pressure and Air Quality Every Hour.

- **Data source:** [Open-Meteo](https://open-meteo.com/)
- **Update frequency:** every hour, via .[cron-job](https://cron-job.org/)
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
**Last updated:** `2026-11-17 07:30:34 UTC`

| Metric | Value |
|---|---|
| 🌡️ Temperature | 24.6 °C |
| 💧 Humidity | 43 % |
| 🌧️ Rain (last hr) | 0.0 mm |
| 💨 Wind Speed | 14.9 km/h |
| 🧭 Wind Direction | 301° |
| 🔵 Pressure | 989.7 hPa |
| 🌫️ AQI (US) | 160 — Unhealthy 🔴 |
| PM2.5 | 29.3 µg/m³ |
| PM10 | 31.2 µg/m³ |

<details><summary>Last 24 readings</summary>

| Time (UTC) | Temp °C | Rain mm | AQI | Wind km/h | Humidity % |
|---|---|---|---|---|---|
| 2026-11-17 07:30:34 | 24.6 | 0.0 | 160 | 14.9 | 43 |
| 2026-11-17 06:30:35 | 23.8 | 0.0 | 161 | 12.6 | 49 |
| 2026-11-17 05:30:31 | 22.3 | 0.0 | 162 | 9.2 | 55 |
| 2026-11-17 04:30:32 | 20.2 | 0.0 | 164 | 7.3 | 61 |
| 2026-11-17 03:30:30 | 17.8 | 0.0 | 166 | 6.9 | 69 |
| 2026-11-17 01:30:37 | 13.9 | 0.0 | 170 | 7.8 | 81 |
| 2026-11-16 23:30:33 | 14.5 | 0.0 | 174 | 7.7 | 75 |
| 2026-11-16 22:30:35 | 14.9 | 0.0 | 176 | 8.3 | 72 |
| 2026-11-16 21:30:34 | 15.3 | 0.0 | 175 | 8.2 | 70 |
| 2026-11-16 20:30:40 | 15.6 | 0.0 | 177 | 7.9 | 68 |
| 2026-11-16 19:30:32 | 15.8 | 0.0 | 180 | 8.8 | 66 |
| 2026-11-16 18:30:33 | 16.3 | 0.0 | 182 | 9.5 | 63 |
| 2026-11-16 17:30:34 | 16.8 | 0.0 | 184 | 9.6 | 62 |
| 2026-11-16 15:30:38 | 17.8 | 0.0 | 188 | 8.6 | 61 |
| 2026-11-16 14:30:33 | 18.7 | 0.0 | 189 | 9.1 | 58 |
| 2026-11-16 12:30:44 | 20.2 | 0.0 | 190 | 8.5 | 65 |
| 2026-11-16 11:30:34 | 22.0 | 0.0 | 190 | 10.1 | 61 |
| 2026-11-16 09:30:38 | 24.8 | 0.0 | 188 | 16.3 | 47 |
| 2026-11-16 08:30:33 | 25.2 | 0.0 | 188 | 16.2 | 45 |
| 2026-11-16 07:30:37 | 24.9 | 0.0 | 188 | 14.7 | 50 |
| 2026-11-16 06:30:34 | 23.8 | 0.0 | 187 | 12.7 | 57 |
| 2026-11-16 05:30:34 | 22.2 | 0.0 | 186 | 11.0 | 67 |
| 2026-11-16 04:30:33 | 20.2 | 0.0 | 185 | 9.6 | 80 |
| 2026-11-16 03:30:33 | 18.2 | 0.0 | 183 | 8.5 | 91 |

</details>
<!-- DATA-END -->

## 📈 Full-Day Trend

Every logged metric for yesterday (the last fully completed day, midnight-to-midnight IST), normalized to its own range so temperature, AQI, humidity, and the rest can be compared by shape on one chart. Only changes once a day, when a new day rolls over.

![Full-day trend chart](data/day_chart.png)

## 🗂️ Chart History

Every day's full-day trend chart, newest first. No retention limit — this grows forever.

<!-- HISTORY-START -->
<details><summary>Last 102 day(s)</summary>

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
