from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/inform')
def inform():
    return "<h1>Страница с подробностями</h1>"

if __name__ == "__main__":
    app.run()