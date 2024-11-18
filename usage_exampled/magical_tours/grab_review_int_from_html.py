import re
import os
import csv

def extract_integers_from_html(html_content, g_number, d_number):
    # Update the regex pattern based on user input
    pattern = rf'href="/ShowUserReviews-g{g_number}-d{d_number}-r(\d+)-'
    # Find all matches in the HTML content
    matches = re.findall(pattern, html_content)
    # Convert the matches to integers
    return [int(match) for match in matches]

def main():
    # Ask user for the numbers after "g" and "d"
    g_number = input("Enter the number after 'g': ")
    d_number = input("Enter the number after 'd': ")
    
    # Directory containing the script and HTML files
    current_dir = os.getcwd()

    # Initialize a list to store extracted review numbers
    all_reviews = []

    # Iterate through all files in the current directory
    for file_name in os.listdir(current_dir):
        if file_name.endswith(".html"):
            file_path = os.path.join(current_dir, file_name)
            with open(file_path, "r", encoding="utf-8") as file:
                html_content = file.read()
                # Extract integers from the current HTML file
                extracted_integers = extract_integers_from_html(html_content, g_number, d_number)
                # Add results to the list
                all_reviews.extend(extracted_integers)

    # Write results to a CSV file
    output_file = "extracted_reviews.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(["review_url"])
        # Write each extracted review URL
        for review in all_reviews:
            review_url = f"https://www.tripadvisor.com/ShowUserReviews-g{g_number}-d{d_number}-r{review}-Magical_History_Tour-Minneapolis_Minnesota.html"
            csv_writer.writerow([review_url])  # Correctly write as a list

    print(f"\nExtraction complete. Data written to {output_file}")

if __name__ == "__main__":
    main()
