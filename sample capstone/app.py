from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/student/login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Dummy logic: Replace this with actual authentication
        if username == '1234567890' and password == 'password123':
            return redirect(url_for('student_homepage'))
        else:
            return 'Invalid credentials. Please try again.'

    return render_template('Student/student_login.html')

@app.route('/student_homepage.html')
def student_homepage():
    return render_template('Student/student_homepage.html')

