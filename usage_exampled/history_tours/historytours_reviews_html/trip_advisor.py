import undetected_chromedriver as uc
import time
import csv
import random

# Function to read links from the CSV file
def read_links_from_csv(file_path):
    links = []
    try:
        with open(file_path, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                links.append(row["Links"])
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return links

# Read links from the CSV file
csv_file = input("Provide path to CSV which contains a TripAdvisor list of links to scrape: ")
links = read_links_from_csv(csv_file)

def scrape_link(link, idx):
    # Create a new ChromeOptions object for each instance
    options = uc.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    
    # Start a new Chrome session
    driver = uc.Chrome(options=options)
    try:
        # Navigate to the link
        driver.get(link)
        rand = random.randint(2, 10)
        time.sleep(rand)
        # Wait for user input before grabbing HTML
        if(idx==1 or idx==2 or idx == 3):
            input(f"Press Enter to grab the HTML of page {idx}...")
        else:
            print(f"Page {idx}...")
        # Get the HTML content of the current page
        html_content = driver.page_source

        # Save the HTML content to a file named "<index>.html"
        file_name = f"{idx}.html"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(html_content)

        print(f"HTML content of {link} saved to {file_name}")
    except Exception as e:
        print(f"Failed to process {link}: {e}")
    finally:
        # Close the browser completely
        driver.quit()

# Iterate through the list of links
for idx, link in enumerate(links, start=1):  # Start naming files from "1.html"
    scrape_link(link, idx)
    time.sleep(2)  # Optional delay between restarts
