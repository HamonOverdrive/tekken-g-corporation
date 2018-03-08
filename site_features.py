import pandas as pd
from bs4 import BeautifulSoup


def inject_frame_data(character):
    'Injects frame data tables to website'
    # get data frame of character csv into html format object for jinja uncomment for local practice
    # df1 = pd.read_csv(fr'/home/rlee/PycharmProjects/tekken-g-corporation/static/char_csvs2/{character}1.csv')
    # df2 = pd.read_csv(fr'/home/rlee/PycharmProjects/tekken-g-corporation/static/char_csvs2/{character}2.csv')

    # # second one is for python anywhere
    df1 = pd.read_csv(fr'/home/robautomata/tekken-g-corporation/static/char_csvs2/{character}1.csv')
    df2 = pd.read_csv(fr'/home/robautomata/tekken-g-corporation/static/char_csvs2/{character}2.csv')

    # gets rid of Nan date with blanks have to use this so html does not show it
    df1 = df1.fillna('')
    df2 = df2.fillna('')

    # inject data table with new class and border for custom css usage also can be done with other attributes like 'id'
    frame_soup1 = BeautifulSoup(df1.to_html(index=False), "html.parser")
    frame_soup1.find('table')['class'] = 'framedata_table'
    frame_soup1.find('table')['border'] = '0'

    frame_soup2 = BeautifulSoup(df2.to_html(index=False), "html.parser")
    frame_soup2.find('table')['class'] = 'framedata_table'
    frame_soup2.find('table')['border'] = '0'

    return frame_soup1, frame_soup2