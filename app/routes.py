from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andrea'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in the neighborhood!'
        },
        {
            'author': {'username': 'Andrea'},
            'body': 'Saw a super hot dude at the gym today.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
