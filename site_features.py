import os, pandas as pd
from bs4 import BeautifulSoup, Tag


# how csv data can turn into html table https://stackoverflow.com/questions/44320329/converting-csv-to-html-table-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
def inject_frame_data(character):
    'Injects frame data tables to website'

    #this file (site_features.py) must remain in the root folder of the site or this variable dir_path must be altered
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # get data frame of character csv into html format object
    df1 = pd.read_csv(fr'{dir_path}/static/char_csvs2/{character}1.csv')
    df2 = pd.read_csv(fr'{dir_path}/static/char_csvs2/{character}2.csv')

    # gets rid of Nan date with blanks have to use this so html does not show it
    df1 = df1.fillna('')
    df2 = df2.fillna('')

    # inject data table with new class and border for custom css usage also can be done with other attributes like 'id'
    frame_soup1 = BeautifulSoup(df1.to_html(index=False), "html.parser")
    frame_soup1 = customizeParsedHtmlTalbe(frame_soup1, tableNo=1)


    frame_soup2 = BeautifulSoup(df2.to_html(index=False), "html.parser")
    frame_soup2 = customizeParsedHtmlTalbe(frame_soup2, tableNo=2)

    return frame_soup1, frame_soup2

def customizeParsedHtmlTalbe(dataTable, tableNo):

    # #customize headers (for sorting arrows)
    # for thRow in dataTable.find_all('th'):
    #
    #     # Building this HTML to replace the <th></th>:
    #     #<th class="move-table-th">
    #     #    <p class="move-table-column-name"> + thRow.string + </p>
    #     #    <span class="move-table-arrow-container">
    #     #        <div class="arrow-up" onclick="sort(this)"></div>
    #     #        <div class="arrow-down" onclick="sort(this)"></div>
    #     #    </span>
    #     #</th>
    #
    #     pTag = Tag(dataTable, name="p")
    #     pTag['class'] = 'move-table-column-name'
    #     pTag.string = thRow.string
    #
    #     spanTag = Tag(dataTable, name="span")
    #     spanTag['class'] = 'move-table-arrow-container'
    #
    #     divUpTag = Tag(dataTable, name="div")
    #     divUpTag['class'] = 'arrow-up'
    #     divUpTag['onclick'] = 'sort(this)'
    #
    #     divDownTag = Tag(dataTable, name="div")
    #     divDownTag['class'] = 'arrow-down'
    #     divDownTag['onclick'] = 'sort(this)'
    #
    #     spanTag.insert(0, divUpTag)
    #     spanTag.insert(1, divDownTag)
    #
    #     thRow.string = ''   #clean the old value
    #     thRow.insert(0, pTag)
    #     thRow.insert(1, spanTag)


    #add id (they should be different for all the tables), class and border to the table
    dataTable.find('table')['id'] = 'framedata_table_' + str(tableNo)
    dataTable.find('table')['class'] = 'framedata_table'
    dataTable.find('table')['border'] = '0'

    return dataTable
