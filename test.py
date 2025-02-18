from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_statistics import Statistics

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)


class Request(db.Model):
    __tablename__ = "request"

    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    response_time = db.Column(db.Float)
    date = db.Column(db.DateTime)
    method = db.Column(db.String)
    size = db.Column(db.Integer)
    status_code = db.Column(db.Integer)
    path = db.Column(db.String)
    user_agent = db.Column(db.String)
    remote_address = db.Column(db.String)
    exception = db.Column(db.String)
    referrer = db.Column(db.String)
    browser = db.Column(db.String)
    platform = db.Column(db.String)
    mimetype = db.Column(db.String)
    rtf = db.Column(db.Float)


db.session.query(Request).delete()
db.session.commit()
db.create_all()

statistics = Statistics(app, db, Request)


@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run()