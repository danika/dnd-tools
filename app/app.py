from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager, login_required, login_user
from models import *
from forms import *


#------App Setup------
app = Flask(__name__)
app.secret_key = 'In peace, vigilance. In war, victory. In death, sacrifice.'
bootstrap = Bootstrap(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = '/login'

#------Assorted Functions------

@login_manager.user_loader
def load_user(user_id):
    return User.load(users_db, str(user_id))

def get_user_id(email):
	vr = users_db.view('search/email', key=email)
	if vr.rows:
		return vr.rows[0].value
	else:
		return None


#------Views-------

#database.view('category/viewname',key='')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
	form = SignUpForm()
	if form.validate_on_submit():
		email = form.email.data
		name = form.name.data
		pwd = form.pwd1.data

		if get_user_id(email) is not None:
			#user already exists
			flash('That email is currently in use.', 'danger')
			return redirect(url_for('signup'))
		else:
			#make new user
			new_user = User(email=email, name=name, password_hash=generate_password_hash(pwd))
			new_user.store(users_db)
			flash('Welcome ' + name + '!', 'success')
			return redirect(url_for('login'))
	return render_template('welcome.html', form=form, action='sign up', 
		alt="<a href='/login'>login</a>")


@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		pwd = form.pwd.data
		
		#attempt to get a user from the email entered
		user = load_user(get_user_id(email))
		if user is not None and user.verify_password(pwd):
			#user exists, password is correct
			flash('Welcome back, ' + user.name + '!', 'success')
			login_user(user)
			return redirect(url_for('main'))
		else:
			#user doesn't exist or password is incorrect
			flash('Invalid email or password.', 'danger')
			return redirect(url_for('login'))
	return render_template('welcome.html', form=form, action='login', 
		alt="<a href='/signup'>sign up</a>")

@app.route('/add-item', methods=['POST', 'GET'])
@login_required
def add_item():
	form = AddItemForm()
	if form.validate_on_submit():
		flash('Success!', 'success')
		return redirect(url_for('add_item'))
	return render_template('add-item.html', form=form)

@app.route('/', methods=['GET'])
@login_required
def main():	
	return render_template('main.html')


if __name__ == "__main__":
	app.run(debug=True)



