from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the webpage we want to scrape
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')  # Explicitly specifying the parser

soup.find('table') # Find the first table in the HTML
soup.find_all('table')[1] # Find the second table in the HTML
soup.find('table', class_='wikitable sortable') # Find the table with class 'wikitable sortable' in the HTML
table = soup.find_all('table')[1]
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles] # Extract the text from the table headers and strip any leading/trailing whitespace

# Create a new DataFrame with the extracted table headers as columns
df = pd.DataFrame(columns=world_table_titles)

# For each row (excluding the header row), find all the table data and add it to the DataFrame
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data

# Save the DataFrame to a CSV file
df.to_csv('world_table.csv', index=False)
