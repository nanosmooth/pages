# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash



# create our little application :)
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'tihishastobeaC!0n%^$@<>;;;}}}:)'

print "i am here"
@app.route('/')
def index():
 print "now here"
 if not session.get('logged_in'):
    return redirect(url_for('login'))
 else:
    return redirect(url_for('welcome'))

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
 if not session.get('logged_in'):
    return redirect(url_for('index'))
 else:
    return render_template('welcome.html',title='Our Magic',page_title='Our Magic',username=session.get('username'))

@app.route('/musings', methods=['GET', 'POST'])
def musings():
 if not session.get('logged_in'):
    return redirect(url_for('index'))
 else:
    return render_template('musings.html',title='Our Magic',page_title='Our Magic'.title(),username=session.get('username'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    print "yeah error is none"
    print request.method
    if request.method == 'POST':
        print request.form['inputUsername']
        print request.form['inputPassword']

        if request.form['inputUsername'] == 'tejus':
            app_user = 'tejus'
            app_pass = 'remember'
        elif request.form['inputUsername'] == 'monika':
            app_user = 'monika'
            app_pass = 'heartbeat9100498225'

        if request.form['inputUsername'] != app_user:
            error = 'Invalid username'
            print "the username was invalid"
        elif request.form['inputPassword'] != app_pass:
            error = 'Invalid password'
        else:

            session['logged_in'] = True
            session['username'] = request.form['inputUsername']
            print "just before login"
            return redirect(url_for('index'))
    return render_template('login.html',
                         title='LogIn - Its specialized for you',
						 page_title='Our Magic',error=error)
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
