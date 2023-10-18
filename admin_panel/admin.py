import os
from flask import Flask, render_template
from utils.db import RecordedUser, session

app = Flask(__name__, template_folder='templates', static_url_path='', static_folder='static')


@app.route('/')
def index():
    users = session.query(RecordedUser).all()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
