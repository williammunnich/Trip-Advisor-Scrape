from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
import os
import time

# Initialize ChromeDriver with WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the target URL
url = "https://www.tripadvisor.com/Attraction_Review-g43323-d1483044-Reviews-Magical_History_Tour-Minneapolis_Minnesota.html"
driver.get(url)

# Wait for at least 5 seconds and ensure the page loads completely
try:
    # Fixed minimum wait of 5 seconds
    time.sleep(10)

    # Additional wait until the <body> tag is present in the DOM (up to 15 more seconds)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Get the HTML content of the page
    html_content = driver.page_source

    # Extract the base name of the URL
    parsed_url = urlparse(url)
    base_name = os.path.basename(parsed_url.netloc)

    # Save the HTML to a file
    file_name = f"{base_name}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"HTML content saved to {file_name}")

except Exception as e:
    print(f"An error occurred while waiting for the page to load: {e}")

finally:
    # Close the browser
    driver.quit()
