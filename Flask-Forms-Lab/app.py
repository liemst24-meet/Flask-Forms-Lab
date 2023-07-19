from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "liem"
password = "Password123"
facebook_friends=["Loai","Polina","Adan", "George", "Jihad", "Roni", "gilad", "romie","shuster"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		u_name = request.form['username']
		p_word = request.form['password']
		if u_name == username and p_word == password:
			return redirect(url_for('home'))

		else:
			return render_template('login.html')


	else:
		return render_template('login.html')
  
  
@app.route('/home', methods=['GET', 'POST'])  # '/' for the default page
def home():
	return render_template('home.html', friends = facebook_friends)


@app.route('/friends_exists/<string:name>', methods=['GET', 'POST'])  # '/' for the default page
def friends_exists(name):
	if name in facebook_friends:
		return render_template('friend_exists.html', n=name, b=True)
	else:
		return render_template('friend_exists.html', n=name, b=False)





if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)