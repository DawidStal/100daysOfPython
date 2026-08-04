from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "books-collection.db")
db_uri = "sqlite:///" + os.path.abspath(db_path).replace("\\", "/")

# db = sqlite3.connect(db_path)
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=="POST":

        with app.app_context():
            new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()

        print("Book successfully added", new_book)

        return redirect(url_for('home'))

    return render_template("add.html")


@app.route("/edit/<book_id>", methods=["GET", "POST"])
def update(book_id):
    book_to_update = db.get_or_404(Book, book_id) 
    if request.method=="POST":
        print(f"Update book {book_to_update.title} to rating", request.form["rating"])  
        book_to_update.rating = float(request.form["rating"])
        db.session.commit()
        
        return redirect(url_for('home'))
    
    return render_template('update.html', book = book_to_update)


@app.route("/delete")
def delete():
    with app.app_context():
        book_id = request.args.get('id')
        book_to_delete =db.get_or_404(Book, book_id) 
        db.session.delete(book_to_delete)
        db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

