from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:lc101@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'GSeVB/.xkffavmur; jvst.lali9jqA'

app.config['POSTS_PER_PAGE_USER'] = 4
app.config['POSTS_PER_PAGE'] = 10

db = SQLAlchemy(app)