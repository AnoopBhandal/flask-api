from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ludocyig:k0aYvDTT3JDc9DBQNqsFul9yZ3qI4LaC@trumpet.db.elephantsql.com/ludocyig'
db = SQLAlchemy(app)


from application import routes