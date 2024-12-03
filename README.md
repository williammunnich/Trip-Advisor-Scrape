# **TripAdvisor Review Scraper**

This project provides a step-by-step process to scrape and extract review data from TripAdvisor. It includes several Python scripts that automate the generation of links, downloading HTML content, and parsing the data into structured formats like CSV files.

---

# **Contents**

1. Overview  
2. Workflow  
3. Scripts Overview  
   - `make_macro_links.py`  
   - `trip_advisor_scrape.py`  
   - `create_valid_links_for_individual_reviews_from_html_local.py`  
   - `extract_review_data.py`  
4. Output  
5. Dependencies  
6. Notes  

---

# 1. **Overview**

The TripAdvisor Review Scraper is a multi-step pipeline:
1. Generate initial links for scraping review pages.  
2. Download HTML pages containing the review data.  
3. Extract individual review links from the downloaded HTML files.  
4. Parse and export review content into a CSV file for further analysis.

---

# 2. **Workflow**

1. **Generate Links**  
   - Run `make_macro_links.py` to generate the links for review pages. The script outputs a CSV file containing the links to scrape.

2. **Scrape Review Pages**  
   - Use `trip_advisor_scrape.py` to download HTML pages for the review links from the previous step. This will save HTML files locally for further processing.  
   - *Note: This step can take a long time.*

3. **Extract Individual Review Links**  
   - Execute `create_valid_links_for_individual_reviews_from_html_local.py` to extract valid individual review links from the saved HTML files. The script outputs a CSV file of these links.

4. **Extract Review Data**  
   - Run `extract_review_data.py` to scrape the individual review pages. The output is a structured CSV file containing review metadata, such as reviewer names, ratings, and content.  
   - *Note: This step can also take a long time.*

---

# 3. **Scripts Overview**

### **1. make_macro_links.py**
**Purpose:**  
Generates the initial list of links for the TripAdvisor review pages based on user input.  

**Input:**  
- TripAdvisor `g` and `d` numbers, total number of reviews, and the tour service name.  

**Output:**  
- `macro_links.csv`: A CSV file containing the generated links.

**How to Run:**
```bash
python make_macro_links.py
```

---

### **2. trip_advisor_scrape.py**
**Purpose:**  
Downloads the HTML content of the pages listed in `macro_links.csv`.  

**Input:**  
- A CSV file (`macro_links.csv`) containing TripAdvisor review page links.  

**Output:**  
- HTML files for each page (e.g., `1.html`, `2.html`, etc.).

**How to Run:**
```bash
python trip_advisor_scrape.py
```

---

### **3. create_valid_links_for_individual_reviews_from_html_local.py**
**Purpose:**  
Extracts individual review links from the downloaded HTML files.  

**Input:**  
- A folder containing the HTML files downloaded in the previous step.  

**Output:**  
- `links.csv`: A CSV file containing links to individual reviews.  

**How to Run:**
```bash
python create_valid_links_for_individual_reviews_from_html_local.py
```

---

### **4. extract_review_data.py**
**Purpose:**  
Parses individual review HTML files to extract fields such as reviewer names, ratings, and review content.  

**Input:**  
- A folder containing individual review HTML files.  

**Output:**  
- `scraped_reviews.csv`: A CSV file containing the extracted review data.  

**How to Run:**
```bash
python extract_review_data.py
```

---

# 4. **Output**

- **`macro_links.csv`**: Contains generated links to TripAdvisor review pages.  
- **HTML files**: Saved HTML files from the review pages and individual reviews.  
- **`links.csv`**: A CSV file containing links to individual reviews.  
- **`scraped_reviews.csv`**: A structured CSV file with extracted review data, including fields like reviewer name, review title, rating, review date, and content.

---

# 5. **Dependencies**

Ensure the following Python libraries are installed:
- `csv`
- `os`
- `re`
- `time`
- `random`
- `beautifulsoup4`
- `undetected_chromedriver`

Install the required libraries using:
```bash
pip install -r requirements.txt
```

Additionally, you'll need Selenium and ChromeDriver for browser automation:

1. **Install Selenium:**
   Use pip to install the Selenium package:
   ```bash
   pip install selenium
   ```

2. **Install ChromeDriver:**
   - **Download ChromeDriver:**  
     Visit the [ChromeDriver Downloads page](https://developer.chrome.com/docs/chromedriver/downloads) and download the version that matches your installed Chrome browser version.
   - **Install ChromeDriver:**  
     After downloading, move the `chromedriver` executable to a directory included in your system's PATH.  
     For example, on Unix-based systems:
     ```bash
     sudo mv chromedriver /usr/local/bin/
     ```
     Ensure the `chromedriver` file is executable:
     ```bash
     sudo chmod +x /usr/local/bin/chromedriver
     ```

**Additional Resources:**
- For detailed instructions on setting up ChromeDriver, refer to the official [Getting Started with ChromeDriver](https://developer.chrome.com/docs/chromedriver/get-started) guide.
- The Selenium documentation provides comprehensive information on [WebDriver](https://www.selenium.dev/documentation/webdriver/getting_started/).

---

# 6. **Notes**

- The scraping steps (especially `trip_advisor_scrape.py` and `extract_review_data.py`) can be time-consuming, as they involve downloading and processing large amounts of data.  
- **Ethics Disclaimer:** Ensure you have permission to scrape data from the website and adhere to their terms of service.  
- Save all CSV files and HTML files in organized folders to maintain a clear workflow.