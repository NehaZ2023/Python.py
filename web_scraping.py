import requests
from bs4 import BeautifulSoup
import pandas as pd

# Specify the URL to scrape
url = "https://example.com"  # Replace with your target URL

# Fetch the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# **Scrape all the text:**
all_text = soup.get_text()
print("All text:", all_text)

# **Scrape a particular div:**
target_div = soup.find("div", {"id": "target-div"})  # Replace with your target div
div_text = target_div.get_text()
print("Div text:", div_text)

# **Scrape all the tables:**
tables = soup.find_all("table")
table_data = []
for table in tables:
    rows = table.find_all("tr")
    table_rows = []
    for row in rows:
        cells = row.find_all("td")
        table_row = [cell.text.strip() for cell in cells]
        table_rows.append(table_row)
    table_data.append(table_rows)

# Create a DataFrame from the table data
df = pd.DataFrame(table_data[1:], columns=table_data[0])  # Skip header row
print(df)