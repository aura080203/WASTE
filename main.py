from flask import Flask, session, redirect, url_for, request, render_template, flash, jsonify

app = Flask(__name__)

# Secret key is needed to keep the client-side sessions secure
app.secret_key = 'supersecretkey'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Logged in as {username}'
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the request
        username = data.get('username')  # Extract username from JSON data

        if username:
            session['username'] = username
            flash('You were successfully logged in')
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Login failed, username is required"}), 400

    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    flash('You were successfully logged out')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
