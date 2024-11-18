import requests
import datetime
import json
import os
from dotenv import load_dotenv

# Load the .env file again
load_dotenv()
# Define the API key and location ID
THE_KEY = os.getenv('API_KEY')  # Replace with your actual API key
ID = os.getenv('LOCATION_ID')


# Define the URL with query parameters
url = f"https://api.content.tripadvisor.com/api/v1/location/{ID}/reviews?key={THE_KEY}&language=en&limit=5"  # Adjust limit as necessary

# Set headers to accept JSON format
headers = {"accept": "application/json"}

# Make the API request
response = requests.get(url, headers=headers)

# Check if the response is successful
if response.status_code == 200:
    # Get current date and time
    now = datetime.datetime.now()
    
    # Format filename as "YYYYMMDD_HHMMSS_<ID>.json"
    filename = f"{now.strftime('%Y%m%d_%H%M%S')}_{ID}.json"
    
    # Save response data to JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
    
    print(f"Data saved to {filename}")
else:
    print(f"Failed to fetch reviews: {response.status_code} - {response.text}")
