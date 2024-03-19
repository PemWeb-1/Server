from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/begkel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)