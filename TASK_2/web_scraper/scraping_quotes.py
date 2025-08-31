import requests
from bs4 import BeautifulSoup
import csv
import json

# Step 1: Fetch the webpage
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Step 2: Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract data (quotes and authors)
quotes_data = []
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

    quotes_data.append({
        "quote": text,
        "author": author,
        "tags": tags
    })

# Step 4a: Save data to CSV
with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags"])
    writer.writeheader()
    for row in quotes_data:
        writer.writerow(row)

# Step 4b: Save data to JSON
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes_data, f, indent=4, ensure_ascii=False)

print("✅ Scraping complete! Data saved to quotes.csv and quotes.json")
