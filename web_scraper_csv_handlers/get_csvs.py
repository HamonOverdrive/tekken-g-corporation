import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup

# had to removes panda from list as pandas is not given frame data yet
character_list = ["Eliza", "Lee", "Bob", "Nina", "Akuma", "Kazumi", "Master-Raven", "Miguel", "Kuma", "Eddy",
                  "Yoshimitsu", "Dragunov", "Hwoarang", "Law", "Asuka", "Shaheen", "Kazuya", "Heihachi", "Claudio",
                  "Lucky-Chloe", "Lili", "Lars", "King", "Jack7",
                  "Bryan", "Steve", "Paul", "Xiaoyu", "Josie", "Jin", "Devil-Jin", "Katarina", "Gigas", "Leo", "Alisa",
                  "Feng", "Geese"]

for character in character_list:
    char = character.lower()
    res = requests.get(f'http://rbnorway.org/{char}-t7-frames/')
    soup = BeautifulSoup(res.content, 'lxml')
    table1 = soup.find_all('table')[0]
    table2 = soup.find_all('table')[1]
    df1 = pd.read_html(str(table1), thousands='dorya')
    df2 = pd.read_html(str(table2), thousands='dorya')

    # index gets rid of index on side which is not needed
    # note: header=None gets rid of the first row which was numbers as a headers
    df1[0].to_csv(f'{character.lower()}1.csv', index=False, header=None)
    df2[0].to_csv(f'{character.lower()}2.csv', index=False, header=None)

# data = df[0]
# print(data)
# print(df[0].to_csv())
