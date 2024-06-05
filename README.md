# Fog Predictor for Lake Cachuma

## Overview

This project is a Flask-based web application that predicts the likelihood of fog at Lake Cachuma, CA. The significance of this prediction is critical for the UCSB rowing team, which has to drive 35 minutes to the lake at 5:15 am. Often, they are unable to row due to foggy conditions, resulting in wasted time and effort. This application aims to solve that problem by providing accurate fog predictions based on machine learning models trained on web-scraped weather data.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Implementation Details](#implementation-details)
- [Significance](#significance)
- [Contributing](#contributing)

## Features

- **Web Scraping**: Scrapes weather data from a reliable source.
- **ML Model Predictions**: Uses trained machine learning models to predict fog.
- **Web Interface**: User-friendly web interface for viewing predictions.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fog-predictor.git
   cd fog-predictor
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application locally**:
   ```bash
   python run.py
   ```

2. **Access the application**:
   Open your browser and go to `http://127.0.0.1:5000/`.

## Project Structure

```
my_flask_app/
├── .ebextensions/
│   └── python.config
├── app/
│   ├── __pycache__/
│   ├── templates/
│   │   └── ...
│   ├── __init__.py
│   ├── model.py
│   ├── routes.py
│   └── utils.py
├── saved_models/
│   ├── image_model_scripted.pt
│   └── mlp_model_scripted.pt
├── static/
│   └── styles.css
├── tests/
│   ├── __init__.py
│   └── test_service.py
├── Procfile.sh
├── README.md
├── requirements.txt
├── run.py
├── runTerminal.py
└── runtime.txt
```

- `.ebextensions/`: Configuration for AWS Elastic Beanstalk.
- `app/`: Contains the main application code.
- `saved_models/`: Pre-trained machine learning models.
- `static/`: Static files like CSS.
- `tests/`: Unit tests for the application.
- `Procfile.sh`: Script for running the application (not used with Heroku).
- `README.md`: Project documentation.
- `requirements.txt`: Lists the project dependencies.
- `run.py`: Entry point for the Flask application.
- `runTerminal.py`: Additional script for running the application.
- `runtime.txt`: Specifies the Python runtime version.

## Implementation Details

### Web Scraping

The application uses BeautifulSoup to scrape weather data from a reliable source. The data includes temperature, humidity, dew point, wind speed, and sky condition.

### Machine Learning Models

1. **Image Model**: Trained to recognize foggy conditions from images.
2. **MLP Model**: Uses weather data points (temperature, humidity, dew point, etc.) to predict fog probability.

### Prediction Workflow

1. **Data Collection**: The `getData` function scrapes current weather data and captures an image.
2. **Data Processing**: The data is processed and transformed into a format suitable for the models.
3. **Prediction**: The processed data is fed into the machine learning models to get the prediction results.

## Significance

The UCSB rowing team often drives 35 minutes to Lake Cachuma early in the morning, only to find that they cannot row due to fog. This application provides an accurate prediction of fog conditions, helping the team make informed decisions about their trips. By doing so, it saves time, effort, and resources, and ensures that the team can plan their practice sessions more effectively.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

