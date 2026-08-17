from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "instance", "users.db")
db_uri = "sqlite:///" + os.path.abspath(db_path).replace("\\", "/")
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form['email']
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if user:
            flash("That email is already registered.")
            return render_template("register.html")
        new_user = User(
            email=email,
            password=generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8),
            name=request.form['name']
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))

        flash("Invalid email or password.")

    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    directory = os.path.join("static", "files")
    return send_from_directory(directory=directory, path='cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
