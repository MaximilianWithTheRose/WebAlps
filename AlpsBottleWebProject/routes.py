"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/mountain')
@view('mountain')
def preview():
    """Renders the about page."""
    return dict(
        title='mountain',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/image')
@view('test')
def preview():
    """Renders the about page."""
    return dict(
        title='image',
        message='Your application description page.',
        year=datetime.now().year
    )
