# Social Media Trend Analytics — Trend Forecaster

An interactive social media analytics dashboard developed using Python, Dash, Plotly, and Pandas to explore word frequencies and hourly activity patterns in historical Twitter data.

## Project Overview

Trend Forecaster is an academic data analytics project designed to transform social media text into interactive visual insights. The dashboard allows users to search for keywords or hashtags, explore frequently occurring words, and examine tweet activity across different hours of the day.

The application uses a locally stored CSV dataset rather than a live social media API.

## Key Features

- **Keyword Search:** Filter tweets using case-insensitive keyword or hashtag searches.
- **Trending Words:** Identify and visualize the ten most frequently occurring words.
- **Hourly Activity Analysis:** Display tweet counts by hour using an interactive line chart.
- **Summary Metrics:** Show the most frequently used word, tweet activity, total dataset records, and unique users.
- **Interactive Dashboard:** Explore data through Plotly visualizations.
- **Automatic Refresh:** Recalculate dashboard visualizations every 60 seconds using the loaded dataset.
- **Dark-Themed Interface:** Responsive dashboard built with Dash Bootstrap Components.

## Technology Stack

- **Programming Language:** Python
- **Data Processing:** Pandas
- **Web Dashboard:** Dash
- **Data Visualization:** Plotly
- **UI Components:** Dash Bootstrap Components
- **Data Format:** CSV

## Dashboard Preview

### Dashboard Overview

![Trend Forecaster Dashboard](ScreenShots/Screenshot%20%2891%29.png)

### Trending Words and Hourly Activity

![Trend Analytics Charts](ScreenShots/Screenshot%20%2892%29.png)

## How It Works

1. The application loads historical tweet data from a CSV file.
2. Tweet timestamps are converted into datetime values, and the hour is extracted.
3. Users can enter a keyword or hashtag to filter tweet text.
4. Word frequencies are calculated from the selected tweets.
5. Tweet counts are aggregated by hour.
6. The results are displayed through summary cards and interactive charts.

## Installation and Usage

Install the required Python libraries:

```bash
pip install pandas dash plotly dash-bootstrap-components
```

Place a compatible dataset named `twitter_dataset.csv` in the same directory as `trend_detection_app.py`.

The CSV must contain at least these columns:

- `tweet`
- `username`
- `created_at`

The `created_at` values should follow the format `DD-MM-YYYY HH:MM`.

Run the application:

```bash
python trend_detection_app.py
```

Open the local address displayed by Dash in your browser.

**Compatibility note:** The application is preserved as originally developed. Its startup command uses `app.run_server()`, which may require an older compatible Dash release.

## Limitations

- The application analyzes a static CSV dataset rather than live Twitter/X data.
- Automatic refresh recalculates the displayed results but does not retrieve new tweets.
- Trending words are identified through basic whitespace tokenization and frequency counting.
- The implementation does not include predictive forecasting, sentiment classification, or trained machine-learning models.
- Search results depend on the contents and quality of the supplied dataset.

## Future Improvements

- Integrate live social media data through authorized APIs.
- Introduce stopword removal and more advanced text preprocessing.
- Add sentiment analysis and topic modeling.
- Implement time-based trend forecasting.
- Expand filtering and dashboard customization.

## Academic Project

**Project:** Trend Forecaster  
**Program:** Bachelor of Technology in Data Science  
**Institution:** Sreenidhi Institute of Science and Technology, Hyderabad, India  
**Year:** 2024  
**Project Type:** Two-member academic team project

Developed collaboratively as part of undergraduate academic work.

## Repository Contents

```text
social-media-trend-analytics/
├── ScreenShots/
├── trend_detection_app.py
├── .gitignore
└── README.md
```

## Purpose

This repository showcases practical experience in Python-based data processing, exploratory text analytics, interactive visualization, and dashboard development.
