import csv

# Function to generate links
def generate_links():
    # Get user inputs
    g_number = input("Enter the number in g (e.g., 43501): ")
    total_reviews = int(input("Enter the total number of reviews: "))
    d_number = input("Enter the number in d (e.g., 3612436): ")
    tour_name = input("Enter the name of the tour service (use underscores for spaces): ")
    or_int = "-orX"
    
    # Calculate the number of pages (links needed)
    number_of_links = (total_reviews // 10) + 1
    
    # Base URL structure
    base_url = f"https://www.tripadvisor.com/Attraction_Review-g{g_number}-d{d_number}{or_int}-Reviews-{tour_name}.html"
    
    # Generate links
    links = []
    for i in range(number_of_links):
        if i == 0:
            links.append(base_url.replace("-orX", ""))
        else:
            links.append(base_url.replace("-orX", f"-or{i*10}"))
    
    # Save links to a CSV file
    with open("macro_links.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Links"])  # Adding header
        for link in links:
            writer.writerow([link])
    
    print(f"{number_of_links} links generated and saved to 'macro_links.csv'")

# Run the function
generate_links()