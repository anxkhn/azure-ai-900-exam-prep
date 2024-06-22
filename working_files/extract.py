# Tool I used to extract the questions and answers from the website

import requests
from bs4 import BeautifulSoup

# Base URL with page parameter
base_url = "https://free-braindumps.com/microsoft/free-ai-900-braindumps.html?p="

# Initialize an empty list to store content
all_content = []

# Loop through all pages from 0 to 34
for page_num in range(35):
    # Construct the full URL
    url = f"{base_url}{page_num}"
    
    # Print the current page being processed
    print(f"Processing page {page_num}...")
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print(f"Successfully retrieved page {page_num}")
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the <div class="content"> and extract its content
        content_div = soup.find('div', class_='content')
        if content_div:
            all_content.append(content_div.prettify())
            print(f"Content found and added for page {page_num}")
        else:
            print(f"No content found for page {page_num}")
    else:
        print(f"Failed to retrieve page {page_num} with status code {response.status_code}")

# Combine all content into a single HTML structure
combined_html = "<html><head><title>Scraped Content</title></head><body>"
combined_html += "".join(all_content)
combined_html += "</body></html>"

# Save the combined content to an HTML file
output_file = "combined_content.html"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(combined_html)

print(f"Content has been successfully scraped and saved to {output_file}")
