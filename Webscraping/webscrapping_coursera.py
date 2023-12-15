# from bs4 import BeautifulSoup
# import requests
# import pandas as  pd
#
# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
#
# popular_languages = pd.DataFrame(columns=["language", "avr_salary"])
# data = requests.get(url).text
#
# soup = BeautifulSoup(data, "html5lib")
#
# table = soup.find('table') # in html table is represented by the tag <table>
#
#
# for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
#     # Get all columns in each row.
#
#     cols = row.find_all('td') # in html a column is represented by the tag <td>
#     language = cols[1].getText() # store the value in column 3 as color_name
#     avr_salary = cols[3].getText() # store the value in column 4 as color_code
#     # print("{}--->{}".format(color_name,color_code))
#
#     popular_languages = pd.concat([popular_languages, pd.DataFrame(
#         {
#             "language": [language],
#             "avr_salary": [avr_salary]
#          }
#     )], ignore_index=True)
#
# print(popular_languages.head())
# popular_languages.to_excel('popular_languages.xlsx')


import requests
from bs4 import BeautifulSoup
import pandas as pd

import requests

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)



url = "https://www.uspa.gov.ua/project/zvit-zerno"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table by inspecting the webpage's HTML source
    table = soup.find('table')

    # Use pandas to read the HTML table into a DataFrame
    if table:
        df = pd.read_html(str(table))[0]

        # Display the DataFrame
        print(df)

        # Save the DataFrame to a CSV file
        df.to_csv('table_data.csv', index=False)

    else:
        print("No table found on the webpage.")

    new_df = df[df['Назва судна'] == 'SEAJOY']
    # new_df = df[['Порт призначення', 'Назва судна']]
    print(new_df.head())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

val = df['Порт призначення'].value_counts()
modee = df['Порт призначення'].mode()

print(val)
print("{}".format(modee))