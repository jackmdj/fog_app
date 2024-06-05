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
- [Research and Model Training](#research-and-model-training)
- [Contributing](#contributing)

## Features

- **Web Scraping**: Scrapes weather data from a reliable source.
- **ML Model Predictions**: Uses trained machine learning models to predict fog.
- **Web Interface**: User-friendly web interface for viewing predictions.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fog_app.git
   cd fog_app
   ```

2. **Create and activate a virtual environment**:
   ```bash
   pip install venv
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the web application**:
   ```bash
   python run.py
   ```

5. **Access the web application**:
   Open your browser and go to `http://127.0.0.1:5000/`.

### Port Forwarding Setup

To make your local Flask server accessible from the internet, you need to set up port forwarding on your router. Here's how you can do it:

1. **Find Your Local IP Address**:
   - On Windows: Open Command Prompt and run `ipconfig`. Look for the IPv4 address under your network connection.
   - On macOS/Linux: Open Terminal and run `ifconfig` or `ip addr`. Look for the `inet` address under your active network connection.

2. **Access Your Router Settings**:
   - Open your web browser and go to your router's admin interface. This is typically at `http://192.168.1.1` or `http://192.168.0.1`.
   - Log in with your router's username and password.

3. **Set Up Port Forwarding**:
   - Find the port forwarding section in your router settings (this can vary by router model).
   - Create a new port forwarding rule:
     - **External Port**: 5000 (or another port of your choice)
     - **Internal IP Address**: Your local IP address (from step 1)
     - **Internal Port**: 5000 (or the port your Flask app is running on)
     - **Protocol**: TCP

4. **Save the Port Forwarding Rule**:
   - Save the changes and restart your router if necessary.

5. **Access Your Flask App**:
   - Use your public IP address to access your Flask app. You can find your public IP address by searching "What is my IP" on Google.
   - Access the app via `http://<your-public-ip>:5000`.

## Project Structure

```
fog_app/
├── app/
│   ├── __pycache__/
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   ├── __init__.py
│   ├── model.py
│   ├── routes.py
│   └── utils.py
├── saved_models/
│   ├── image_model_scripted.pt
│   └── mlp_model_scripted.pt
├── static/
│   └── styles.css
├── README.md
├── requirements.txt
├── run.py
└── runTerminal.py
```

- `app/`: Contains the main application code.
- `saved_models/`: Pre-trained machine learning models.
- `static/`: Static files like CSS.
- `README.md`: Project documentation.
- `requirements.txt`: Lists the project dependencies.
- `run.py`: Entry point for the Flask application.
- `runTerminal.py`: Script for running the application in a terminal

## Implementation Details

### Web Scraping

The application uses BeautifulSoup to scrape weather data from multiple sources. The data includes an image, temperature, humidity, dew point, wind speed, and sky condition.

### Machine Learning Models

1. **Image Model**: Trained to recognize foggy conditions from images.
2. **MLP Model**: Uses weather data points (temperature, humidity, dew point, etc.) to predict fog probability.

### Prediction Workflow

1. **Data Collection**: The `getData` function scrapes current weather data and captures an image.
2. **Data Processing**: The data is processed and transformed into a format suitable for the models.
3. **Prediction**: The processed data is fed into the machine learning models to get the prediction results.

## Research and Model Training

The predictive models used in this application are the result of extensive research and development carried out in a separate repository. This section provides an overview of the process, from data collection to model evaluation.

### Data Collection

The foundational work for this project is documented in the [fog_research](https://github.com/jackmdj/fog_research) repository. The research focused on collecting and analyzing weather data relevant to fog prediction at Lake Cachuma, CA. Key steps included:

1. **Data Collection**: Web scraping techniques were used to gather real-time weather data and an image of the lake.

2. **Data Preprocessing**: The collected data was cleaned, preprocessed, and organized to ensure quality and consistency. Missing values were handled, and relevant features were engineered to improve model performance.

### Model Training

The model training process involved several key stages:

1. **Feature Selection**: Relevant features were selected based on their correlation with fog occurrence. This included weather parameters like temperature, humidity, dew point, and wind speed.

2. **Model Selection**: Different machine learning models were evaluated. The final models selected were:
   - **Image Classification Model**: A Convolutional Neural Network (CNN) based on ResNet-18, trained to recognize foggy conditions from images.
   - **MLP Model**: A custom Multi-Layer Perceptron (MLP) that uses weather data points to predict the probability of fog.

3. **Training and Validation**: The models were trained on the collected data and validated using a separate validation set to ensure they generalize well to new data. Cross-validation techniques were used to fine-tune hyperparameters and improve model performance.

### Model Evaluation

The models were evaluated to ensure they meet the required accuracy and reliability for practical use. The evaluation process included:

1. **Accuracy and Precision**: Metrics such as accuracy, precision, recall, and F1-score were used to assess model performance.

2. **Confusion Matrix**: A confusion matrix was plotted to visualize the performance of the classification models, identifying true positives, false positives, true negatives, and false negatives.

3. **ROC Curve**: The Receiver Operating Characteristic (ROC) curve and Area Under the Curve (AUC) were used to evaluate the model's ability to distinguish between fog and no-fog conditions.

For more detailed information on the research, model training, data collection, and evaluation process, please refer to the [fog_research](https://github.com/jackmdj/fog_research) repository.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

