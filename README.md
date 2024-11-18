make_macro_links.py --> use this to make the initial link for the site, this will give all the pages that the links exist on

trip_advisor_scrape.py --> this will take the data from the output of make_macro_links.py (the CSV file) and save the HTML files from the page to be scraped later *NOTE*this scraping will take a long time*NOTE*

create_valid_links_for_individual_reviews_from_html_local.py --> takes outputed and saved HTML files and spits out a CSV file that contains all the links to the pages with one individual review

extract_review_data.py --> takes the outputed indiviual review HTML and scrape the fields into a CSV file *NOTE*this scraping will take a long time*NOTE*