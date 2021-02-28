from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, ItemForm
from app.models import Employee, Item
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(label=form.label.data, employee_id=current_user.get_id())
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('home.html', title='Home', form=form)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/menu')
def menu():
    items = Item.query.all()
    return render_template("menu.html", items=items)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        employee = Employee(username=form.username.data, password=hashed_password)
        db.session.add(employee)
        db.session.commit()
        flash(f'Account created for {form.username.data}! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(username=form.username.data).first()
        if employee and bcrypt.check_password_hash(employee.password, form.password.data):
            login_user(employee, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template("account.html", title='account')