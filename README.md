# 🌦️ Weather & AQI Logger

Automated weather station — temperature, humidity, wind, pressure, and air quality (AQI), fetched **every hour** via GitHub Actions and logged straight into this repo.

- **Data source:** [Open-Meteo](https://open-meteo.com/) (free, no API key required)
- **Update frequency:** every hour, via `.github/workflows/update-weather.yml`
- **Raw data:** [`data/weather_log.csv`](data/weather_log.csv)

## 📊 Current Conditions

<!-- DATA-START -->
No data logged yet. The workflow runs hourly — check back soon.
<!-- DATA-END -->

## ⚙️ How it works

1. `update-weather.yml` runs on an hourly cron schedule (and can be triggered manually from the Actions tab).
2. `scripts/fetch_weather.py` pulls current weather + AQI from Open-Meteo and appends a row to `data/weather_log.csv`.
3. `scripts/update_readme.py` reads the CSV and rewrites the section above, between the `DATA-START` / `DATA-END` markers.
4. The workflow commits and pushes the updated CSV + README back to the repo.

## 🗺️ Changing the location

Set repository variables under **Settings → Secrets and variables → Actions → Variables**:

| Variable | Description | Default |
|---|---|---|
| `WEATHER_LAT` | Latitude | `28.8500` (Gajraula, UP) |
| `WEATHER_LON` | Longitude | `78.2333` (Gajraula, UP) |

## 🧪 Running locally

```bash
pip install -r requirements.txt
python scripts/fetch_weather.py
python scripts/update_readme.py
```

## 📁 Repo structure

```
weather-logger/
├── .github/workflows/update-weather.yml
├── data/weather_log.csv
├── scripts/fetch_weather.py
├── scripts/update_readme.py
├── README.md
└── requirements.txt
```
