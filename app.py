from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('./utils/config.py')

db = SQLAlchemy(app, metadata=MetaData(schema='YtbDownloader'))

from utils.views import *

if __name__ == '__main__':

    app.run(
        debug=True,
    )