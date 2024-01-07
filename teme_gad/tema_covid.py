import requests
import pandas as pd
from bs4 import BeautifulSoup


def string_clean(string):
    cleaned_string = ''.join(char for char in string if
                             char.isdigit() or char == '.' or char.isalpha() or char.isspace())
    result = float(cleaned_string) if any(char.isdigit() for char in cleaned_string) else cleaned_string.strip()
    return result


header = ['NR.CRT', 'Judet', '10.12', '11.12', '12.12', '13.12', '14.12']
dataset = [header]

url = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-11-decembrie-ora-13-00-2/"
response = requests.get(url)

link = BeautifulSoup(response.text, 'html.parser')


table = link.find('table')
table_content = []
for t_row in table.find_all('tr'):
    for t_data in t_row.find_all('td'):
        table_content.append(t_data.get_text())

for i in range(5):
    table_content.pop(0)

table_content_c = []
for index in range(0, len(table_content), 5):
    table_content_c.append(table_content[index])
    table_content_c.append(table_content[index + 1])
    table_content_c.append(table_content[index + 2])

table_content_c[-1] = table_content_c[-2]
table_content_c[-2] = ' '

table_content_c[-3] = string_clean(table_content_c[-3])
table_content_c[-4] = string_clean(table_content_c[-4])
table_content = table_content_c
print(table_content)
for i in range(0, len(table_content), 3):
    dataset.append([table_content[i], table_content[i + 1], table_content[i + 2]])
df = pd.DataFrame(dataset)
print(df)
df.to_csv('date_covid.csv', index=False, header=False)
