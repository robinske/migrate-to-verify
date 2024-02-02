from flask import Flask, flash, render_template, request
from otp import send, check

app = Flask(__name__)
app.secret_key = 'SUP3R_$ECRET'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_verification():
    phone_number = request.form['phone_number']
    send(phone_number)
    return render_template('check.html', phone_number=phone_number)

@app.route('/check', methods=['POST'])
def check_verification():
    phone_number = request.form['phone_number']
    token = request.form['token']
    approved = check(phone_number, token)

    if approved:
        flash('Approved', 'success')
        return render_template('approved.html')
    else:
        flash('Invalid token', 'error')
        return render_template('check.html', phone_number=phone_number)
    