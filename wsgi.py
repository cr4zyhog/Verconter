from data import db_session
from main import app

db_session.global_init("database/history.db")
if __name__ == '__main__':
    app.run()
