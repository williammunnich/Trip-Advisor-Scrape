import re
import csv
import os

# Path to your folder containing HTML files
html_folder_path = input("Provide the path of the extraxted html files to sort through: ")
# Path to save the CSV file
csv_file_path = "links.csv"

# Define the regular expression pattern
# Match links starting with /ShowUserReviews and capture all content up to .html
pattern = r"/ShowUserReviews.*?\.html"

# List to hold all matched links
all_links = []

# Iterate through all files in the specified folder
for filename in os.listdir(html_folder_path):
    if filename.endswith(".html"):  # Only process .html files
        file_path = os.path.join(html_folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
            # Find all matching links in the file
            matching_links = re.findall(pattern, html_content)
            # Prepend the base URL to each link
            full_links = [f"https://www.tripadvisor.com{link}" for link in matching_links]
            # Add to the master list
            all_links.extend(full_links)

# Save the collected links to a CSV file
with open(csv_file_path, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Write the header
    writer.writerow(["Links"])
    # Write all links
    for link in all_links:
        writer.writerow([link])

# Print confirmation message
if all_links:
    print(f"Saved {len(all_links)} links from folder '{html_folder_path}' to '{csv_file_path}'.")
else:
    print("No matches found. CSV file not created.")