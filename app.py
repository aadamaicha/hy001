from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/wordcloud.html')
def worldcould():  # put application's code here
    return render_template('wordcloud.html')

@app.route('/trend.html')
def trend():  # put application's code here
    return render_template('trend.html')

@app.route('/theme.html')
def theme():  # put application's code here
    return render_template('theme.html')

@app.route('/timeline.html')
def timeline():  # put application's code here
    return render_template('timeline.html')

@app.route('/contact.html')
def contact():  # put application's code here
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()

