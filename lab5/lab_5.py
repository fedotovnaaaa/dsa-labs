from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key_for_lab5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# Модель пользователя для базы данных
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)


# Функция загрузки пользователя для Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Корневая страница GET (если пользователь не авторизован, перенаправляем на вход)
@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html')
    return redirect(url_for('login'))


# Вход (GET + POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            return render_template('login.html', error='Пользователь не найден')
        
        if not check_password_hash(user.password, password):
            return render_template('login.html', error='Неверный пароль')

        login_user(user)
        return redirect(url_for('index'))

    # GET-запрос — показываем форму
    return render_template('login.html')


# Регистрация (GET + POST)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(email=email).first():
            return render_template('signup.html', error='Пользователь с таким ' \
            'email уже существует')

        new_user = User(
            email=email,
            password=generate_password_hash(password),
            name=name
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    # GET-запрос — показываем форму
    return render_template('signup.html')


# Выход
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
