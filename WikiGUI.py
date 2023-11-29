import tkinter as tk
from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_data():
    url = url_entry.get()
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find_all('table')[1]
    world_titles = table.find_all('th')
    world_table_titles = [title.text.strip() for title in world_titles]

    pd.set_option('display.width', 900000000)  # Set the width to desired value

    df = pd.DataFrame(columns=world_table_titles)

    column_data = table.find_all('tr')
    for row in column_data[1:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]

        length = len(df)
        df.loc[length] = individual_row_data

    text.delete(1.0, tk.END)
    text.insert(tk.END, df)

root = tk.Tk()

url_label = tk.Label(root, text="URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

scrape_button = tk.Button(root, text="Scrape Data", command=scrape_data)
scrape_button.pack()

text = tk.Text(root, width=100, height=40)  # Increase width and height as needed
text.pack()

root.mainloop()