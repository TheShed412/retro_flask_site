from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/github')
def github():
    return render_template('github.html')


@app.route('/skills')
def skills():
    return render_template('skill.html')


if __name__ == '__main__':
    app.run()
