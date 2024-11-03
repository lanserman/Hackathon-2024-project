import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.canr.msu.edu/ipm/agriculture/christmas_trees/gdd_of_landscape_insects'  # Replace with your target URL
response = requests.get("https://www.canr.msu.edu/ipm/agriculture/christmas_trees/gdd_of_landscape_insects")
if response.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')  

data = []
headers = [header.text.strip() for header in table.find_all('th')]

for row in table.find_all('tr')[1:]:  
    cells = row.find_all('td')
    if len(cells) == len(headers):  
        row_data = {headers[i]: cells[i].text.strip() for i in range(len(cells))}
        data.append(row_data)

with open('table_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Data has been saved to table_data.json")
