from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import hashlib

from task_4.models import db, User
from task_4.forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

app.config['SECRET_KEY'] = b'ea959bc6bbd140100d66503aa6ac1242c6eb0e8d4c38b85c7ea9a9d2a8e60451'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = hashlib.sha256(form.password.data.encode()).hexdigest()

        existing_user = User.query.filter(User.name == name).first()
        existing_email = User.query.filter(User.email == email).first()

        if existing_user:
            error_msg = 'Такой пользователь существует'
            form.name.errors.append(error_msg)
            return render_template('register.html', form=form)
        if existing_email:
            error_msg = 'Такая почта существует'
            form.email.errors.append(error_msg)
            return render_template('register.html', form=form)

        user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Спасибо за регистрацию!'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
