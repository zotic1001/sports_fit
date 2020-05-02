from flask import Flask, render_template, redirect, request, make_response, session, abort, url_for
from data import db_session
from data.users import User
from data.traning_program import Traning
from registerform import RegisterForm
from loginform import LoginForm
from changeform import ChangeForm
from training_form import TraningForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_restful import reqparse, abort, Api, Resource
import users_resource
import traning_resource
from sport_func import ideal_weight, set_category, goal




app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
api = Api(app)
app.config["SECRET_KEY"] = "secret-key"

def main():
    db_session.global_init("db/blogs.sqlite")
    # для списка объектов
    api.add_resource(users_resource.UserListResource, '/users/')
    # для одного объекта
    api.add_resource(users_resource.UsersResource, '/users/<int:user_id>')
    api.add_resource(traning_resource.TraningResource, "/traning/<int:prog_id>")
    api.add_resource(traning_resource.TraningListResource, "/traning")
    app.run()


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@login_required
@app.route("/lk")
def lk():
    return render_template("lk.html", user=current_user, title="Личный кабинет", goal=goal(current_user.height, current_user.weight,
                                                                                           current_user.age, current_user.gender, current_user.body_type))
@app.route("/add_program", methods=["GET", "POST"])
def add_program():
    form = TraningForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        traning = Traning(
            title=form.title.data,
            duration=form.duration.data,
            category=form.category.data,
            program=form.program.data
        )
        session.add(traning)
        session.commit()
        return redirect("/")
    return render_template("programs_add.html", form=form, title="Добавление программы")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)



@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            height=form.height.data,
            weight=form.weight.data,
            gender=form.gender.data,
            need=form.need.data,
            body_type=form.body_type.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        login_user(user, True)
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@login_required
@app.route("/programs")
def programs():
    session = db_session.create_session()
    prog = session.query(Traning)
    goas = goal(current_user.height, current_user.weight, current_user.age, current_user.gender, current_user.body_type)
    hk = ""
    if "M" in set_category(current_user.gender, goas):
        hk += "Мужчина "
    else:
        hk += "Женщина "
    if "M" in set_category(current_user.gender, goas):
        if "N" in set_category(current_user.gender, goas):
            hk += "нормального веса"
        elif "VF" in set_category(current_user.gender, goas):
            hk += "очень полный"
        elif "VT" in set_category(current_user.gender, goas):
            hk += "очень худой"
        elif "F" in set_category(current_user.gender, goas):
            hk += "полный"
        elif "S" in set_category(current_user.gender, goas):
            hk += "спортивный вес"
        elif "T" in set_category(current_user.gender, goas):
            hk += "худой"
    else:
        if "N" in set_category(current_user.gender, goas):
            hk += "нормального веса"
        elif "VF" in set_category(current_user.gender, goas):
            hk += "очень полная"
        elif "VT" in set_category(current_user.gender, goas):
            hk += "очень худая"
        elif "F" in set_category(current_user.gender, goas):
            hk += "полная"
        elif "S" in set_category(current_user.gender, goas):
            hk += "спортивный вес"
        elif "T" in set_category(current_user.gender, goas):
            hk += "худая"

    return render_template("programs.html", prog=prog, category=set_category(current_user.gender, goas), hk=hk)

@login_required
@app.route('/change', methods=['GET', 'POST'])
def change():
    session = db_session.create_session()
    form = ChangeForm()
    if form.validate_on_submit():
        rows = session.query(User).filter(User.id == current_user.id).update({'weight': form.weight.data, "height": form.height.data, "age": form.age.data, "need": form.need.data})
        session.commit()
        return redirect('/lk')
    return render_template('change.html', title='Изменение', form=form, current_user=current_user)


@app.route("/")
def title():
    return render_template("title.html")
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

if __name__ == '__main__':
    main()
    app.run()