import torch
from torchvision import transforms
from bs4 import BeautifulSoup
import re
import requests
from PIL import Image
from io import BytesIO

def download_image():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
    image_url = 'https://www.805webcams.com/cameras/cachumalake/camera.jpg'
    try:
        image_response = requests.get(image_url, headers=headers, stream=True)
        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            return image

    except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")            

def transform(image):
    mean = [0.565084, 0.56311, 0.572931]
    sd = [0.246431, 0.24439, 0.25317]
    transform_pipeline = transforms.Compose([
        transforms.Resize((256, 256)),  
        transforms.ToTensor(), 
        transforms.Normalize(mean, sd)
    ])
    transformed_image = transform_pipeline(image)
    return transformed_image

def getImageData():
    image = download_image()
    image = transform(image)
    return image

def getString():
    url = 'https://www.localconditions.com/weather-lake-cachuma-california/93464/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            weather_text_element = soup.find(id='readLCWXtxt')
            return weather_text_element.get_text(strip=True)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def parse(text):
    temperature_pattern = r"It is (\d+) degrees fahrenheit"
    humidity_pattern = r"humidity is (\d+\.?\d*) percent"
    dew_point_pattern = r"dew point of (\d+\.?\d*) degrees fahrenheit"
    trend_pattern = r"that is (\w+) since the last report"
    
    # Extract data using regular expressions
    temperature_match = re.search(temperature_pattern, text)
    humidity_match = re.search(humidity_pattern, text)
    dew_point_match = re.search(dew_point_pattern, text)
    trend_match = re.search(trend_pattern, text)
    
    # Extract values from match groups
    temperature = float(temperature_match.group(1))
    humidity = float(humidity_match.group(1))
    dew_point = float(dew_point_match.group(1))
    trend_str = trend_match.group(1)

    # Encode categorical data
    trend_mapping = {'steady': 2, 'rising': 1, 'falling': 0}
    trend = float(trend_mapping[trend_str])

    # Create tensor
    data = torch.tensor([temperature, humidity, dew_point, trend], dtype=torch.float32)
    return data
    
def getTextData():
    textString = getString()
    textData = parse(textString)
    return textData, textString

def getData():
    textData, textString = getTextData()
    image = getImageData()
    return textData, textString, image

def printText(text):
    # Define regex patterns
    temperature_pattern = r"It is (\d+) degrees fahrenheit"
    dew_point_pattern = r"dew point of (\d+\.?\d*) degrees fahrenheit"
    wind_pattern = r"Wind direction is (\w+) at (\d+) miles per hour, gusting at (\d+) mph"
    sunrise_pattern = r"Sunrise is at (\d{1,2}:\d{2} \w{2})"
    sky_condition_pattern = r"has a sky condition of ([\w\s]+) with"
    humidity_pattern = r"humidity is (\d+\.?\d*) percent"
    
    # Extract data using regular expressions
    temperature_match = re.search(temperature_pattern, text)
    dew_point_match = re.search(dew_point_pattern, text)
    wind_match = re.search(wind_pattern, text)
    sunrise_match = re.search(sunrise_pattern, text)
    sky_condition_match = re.search(sky_condition_pattern, text)
    humidity_match = re.search(humidity_pattern, text)
    
    # Get the matched groups
    temperature = temperature_match.group(1) if temperature_match else "N/A"
    dew_point = dew_point_match.group(1) if dew_point_match else "N/A"
    humidity = humidity_match.group(1) if humidity_match else "N/A"
    wind_direction = wind_match.group(1) if wind_match else "N/A"
    wind_speed = wind_match.group(2) if wind_match else "N/A"
    wind_gust = wind_match.group(3) if wind_match else "N/A"
    sunrise = sunrise_match.group(1) if sunrise_match else "N/A"
    sky_condition = sky_condition_match.group(1) if sky_condition_match else "N/A"
    
    # Print the information in an organized format
    result = (
        f"Weather Report:\n"
        f"Sky Condition: {sky_condition}\n"
        f"Temperature: {temperature} F\n"
        f"Dew Point: {dew_point} F\n"
        f"Humidity: {humidity} %\n"
        f"Wind: {wind_direction} at {wind_speed} mph, gusting at {wind_gust} mph\n"
        f"Sunrise: {sunrise}\n"
        f"ML Fog Predictions:\n"
    )
    
    return result

def printPredictionResults(image_result, mlp_result):
    result = (
        "Image Classifier:\n"
        f"  Accuracy: {image_result['prediction_accuracy']}\n"
        f"  Prediction: {image_result['prediction']}\n\n"
        "MLP:\n"
        f"  Probability of Fog: {mlp_result['probability_of_fog']}\n"
        f"  Prediction: {mlp_result['prediction']}\n"
    )
    return result
