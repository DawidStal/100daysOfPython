from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)

# CREATE DB
db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "movie-collection.db")
db_uri = "sqlite:///" + os.path.abspath(db_path).replace("\\", "/")
os.makedirs(os.path.dirname(db_path), exist_ok=True)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# initialize the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    year: Mapped[int] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    ranking = StringField('Integer', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    img_url = URLField('Image URL')
    submit = SubmitField()

class EditForm(FlaskForm):
    rating = StringField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField()

@app.route("/")
def home():
    with app.app_context():
            result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
            all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=="POST":

        with app.app_context():
            new_movie = Movie(
                title=request.form["title"],
                year=request.form["year"], 
                description=request.form["description"], 
                rating=request.form["rating"],
                ranking=request.form["ranking"],
                review=request.form["review"],
                img_url=request.form["img_url"]
                )
            db.session.add(new_movie)
            db.session.commit()

        return redirect(url_for('home'))

    movie_form = MovieForm()
    return render_template("add.html", form=movie_form)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def update(movie_id):
    movie_to_update = db.get_or_404(Movie, movie_id) 
    if request.method=="POST":
        movie_to_update.rating = float(request.form["rating"])
        movie_to_update.review = request.form["review"]
        db.session.commit()
        
        return redirect(url_for('home'))
    
    edit_form = EditForm()
    return render_template('edit.html', form=edit_form, movie = movie_to_update)

@app.route("/delete")
def delete():
    with app.app_context():
        movie_id = request.args.get('movie_id')
        movie_to_delete =db.get_or_404(Movie, movie_id) 
        db.session.delete(movie_to_delete)
        db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
