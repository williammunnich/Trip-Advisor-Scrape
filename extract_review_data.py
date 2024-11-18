import os
import csv
from bs4 import BeautifulSoup

# Function to extract review data from an HTML file
def extract_review_data(html_content):
    """
    Extracts reviewer name, title, rating, date, and content from the HTML content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    reviews = []
    
    # Find all review containers
    review_containers = soup.find_all('div', id=lambda x: x and x.startswith("review_"))
    
    for container in review_containers:
        try:
            review_id = container['id']  # Extract the dynamic review ID
            reviewer_name = container.select_one('div div:nth-of-type(1) div div div:nth-of-type(2) div:nth-of-type(1)').get_text(strip=True)
            title = soup.select_one('#HEADING').get_text(strip=True)
            
            # Extract rating
            rating_class = container.select_one('div div:nth-of-type(2) span[class*="ui_bubble_rating"]')['class'][1]
            rating = int(rating_class.split('_')[-1]) / 10
            
            # Extract date
            date = container.select_one('div div:nth-of-type(2) div:nth-of-type(4)').get_text(strip=True)
            
            # Extract review content
            content = container.select_one('div div:nth-of-type(2) div:nth-of-type(3) div p span').get_text(strip=True)
            
            # Add extracted data to list
            reviews.append({
                "review_id": review_id,
                "reviewer_name": reviewer_name,
                "title": title,
                "rating": rating,
                "date": date,
                "content": content,
            })
        except AttributeError:
            # Skip if any element is not found
            print(f"Skipping a review in file: missing data.")
    
    return reviews

# Function to process all HTML files in a directory
def process_html_files(directory_path, output_csv):
    """
    Process all HTML files in the given directory and save extracted data to a CSV file.
    """
    all_reviews = []
    
    # Iterate through all files in the directory
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".html"):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, "r", encoding="utf-8") as file:
                html_content = file.read()
                # Extract review data from the current HTML file
                reviews = extract_review_data(html_content)
                all_reviews.extend(reviews)
    
    # Write data to a CSV file
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["review_id", "reviewer_name", "title", "rating", "date", "content"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_reviews)

    print(f"Data saved to {output_csv}")

# Main function
if __name__ == "__main__":
    # Directory containing the HTML files
    html_directory = input("Please give the path of the folder containing the individual review HTMLs: ")
    output_csv_file = "scraped_reviews.csv"

    # Process all HTML files in the directory
    process_html_files(html_directory, output_csv_file)
