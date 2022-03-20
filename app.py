from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

"""
@app.route('/index')
@app.route('/')
def helloworld():
    return "Hello World!"

@app.route('/new/')
def queryString(greetings='Hello'):
    query_val = request.args.get('greetings', greetings)
    return '<h2>Hey {0}<h2>'.format(query_val)

@app.route('/user')
@app.route('/user/<name>')
def noQueryString(name='Yogesh'):
    return '<h2>Hey there! {0}<h2>'.format(name)


@app.route('/watch')
def watchMovies():
    moviesList = [
        'Encanto',
        'Raya:The last dragon',
        'Ramayana',
        'Ravan:The demon king',
        'Karn',
        'Harry pottor'
    ]

    return render_template('movies.html', movies=moviesList, name='Yogesh')


@app.route('/movie_duration')
def movies_plus():
    movies_dict = {
        "Encanto" : 1.45,
        "Raya: The last dragon" : 2.5,
        "Ramayana" : 3.15,
        "Ravan: The demon king" : 1.50,
        "Karn" : 2.30,
        "Harry Potter" : 2.50
    }

    return render_template("table_data.html", movies=movies_dict, name="Yogi")


@app.route('/using_macros')
def using_macros():
    movies_dict = {
        "Encanto" : 1.45,
        "Raya: The last dragon" : 2.5,
        "Ramayana" : 3.15,
        "Ravan: The demon king" : 1.50,
        "Karn" : 2.30,
        "Harry Potter" : 2.50
    }

    return render_template("using_macros.html", movies=movies_dict, name="Yogi")
"""

app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Yuvraj@localhost/book_catlog'
app.debug = True
db = SQLAlchemy(app)

class Publication(db.Model):
    __tablename__ = "publication"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60), nullable= False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Name is {}'.format(self.name)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)