from flask import Flask, render_template, request, session, redirect
from py_firebase import firebase

import datetime

from requests.exceptions import HTTPError

import json


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)


def firebase_error(e):
    return json.loads(e.strerror)['error']['errors'][0]['message']


@app.route('/', methods=['POST', 'GET'])
def index():
    exception = None

    if request.method == 'POST':
        user = None

        try:
            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(
                request.form.get('email'),
                request.form.get('password')
            )
        except HTTPError as e:
            exception = firebase_error(e)

        if user:
            session['user_id'] = user['idToken']

            firebase.database().child('user_logins').push({
                'last_login': datetime.datetime.now().strftime('%s'),
                'email': user['email']
            })

            return redirect('/welcome')

    return render_template('index.html', exception=exception)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
