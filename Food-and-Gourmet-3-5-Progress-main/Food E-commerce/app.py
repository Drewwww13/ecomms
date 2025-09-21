from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/reload')
def reload():
    return render_template("index.html")


# !!!!!!!!!!! Login at Signup !!!!!!!!!!!

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Login Attempt: {email}, {password}")
        flash(f"Welcome back, {email}!")
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(f"New User: {name}, {email}, {password}")
        flash(f"Thanks for signing up, {name}!")
        return redirect(url_for('home'))
    return render_template('signup.html')


# Renz eto yung sa Cart Icon wla pang naka lagay so ako na bahala dine thx
# Nisabi ko lng kasi baka magalaw mo 
@app.route('/cart')
def cart():
    return "<h1>Your cart is empty!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
