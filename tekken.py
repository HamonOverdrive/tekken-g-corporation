from flask import Flask, render_template
from site_features import inject_frame_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

# frame data tables for each character
@app.route('/frame-data/<string:character>')
def frame_page(character):
    frame_soup1, frame_soup2 = inject_frame_data(character)

    return render_template("char_frame_page.html", character=character, ctable1=frame_soup1, ctable2=frame_soup2)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def file_not_found(e):
    return render_template('500.html')


if __name__ == '__main__':
    app.run(debug=False)
