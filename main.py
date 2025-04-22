import os
from pyexpat.errors import messages
import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = '23456fusaftdr68fty32hhwftr6tyJBHFY&RtqgevgutiOHOPU_$$UnWDjk'


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('main.html')


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host='0.0.0.0')


if __name__ == '__main__':
    main()
