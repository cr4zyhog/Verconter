import os
import flask
from data.history import History
from data import db_session

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = '23456fusaftdr68fty32hhwftr6tyJBHFY&RtqgevgutiOHOPU_$$UnWDjk'


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('main.html')


@app.route('/history')
def history():
    db_sess = db_session.create_session()
    history1 = db_sess.query(History).all()
    db_sess.commit()
    return flask.render_template('history.html', history=history1)


@app.route('/converter')
def converter():
    return 'пока не готово'


@app.route('/images/<imagename>')
def image(imagename):
    a = os.getcwd() + f'/images/{imagename}'
    return flask.send_file(a)



def main():
    db_session.global_init("database/history.db")
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host='0.0.0.0')


if __name__ == '__main__':
    main()
