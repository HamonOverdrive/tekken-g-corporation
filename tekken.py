from flask import Flask, render_template
import pandas as pd
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/frame-data/<string:character>')
def frame_page(character):
    # get data frame of character csv into html format object for jinja
    df1 = pd.read_csv(r'C:\Users\Robin\PycharmProjects\tekken\static\char_csvs\{}1.csv'.format(character))
    df2 = pd.read_csv(r'C:\Users\Robin\PycharmProjects\tekken\static\char_csvs\{}2.csv'.format(character))

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

    return render_template("char_frame_page.html", character=character, ctable1=frame_soup1, ctable2=frame_soup2)


if __name__ == '__main__':
    app.run(debug=True)
