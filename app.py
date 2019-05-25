from flask import Flask
from models import db, Alchemy

app = Flask(__name__)
POSTGRES = {
    'user': 'ninanjohn',
    'db': 'sqlalch',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)

@app.route('/')
def main():
    return 'Hello World!'

@app.route("/materials")
def materials():
    alchemy = Alchemy()
    return alchemy.__repr__()

if __name__ == '__main__':
    app.run()