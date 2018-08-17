from functools import wraps
from flask import url_for, redirect, session, flash

def login_required(func):
    """
    decorator to ensure user is authorized
    for operations
    """
    @wraps(func)
    def check_login(*arg, **kwargs):
        """
        checks if user is logged in
        else redirects to home page
        """
        if is_user_authorized():
            return func(*arg, **kwargs)
        else:
            if 'category' in func.__name__:
                flash('You need to login first to create category!')
            else:
                flash('You need to login first to create item!')  
            return redirect(url_for('catalog.display_catalog'))
    return check_login


def user_info():
    """
    Logged in user information
    """
    user = {
        'authorized': False
    }
    if not is_user_authorized():
        print(user)
        return user
    else:
        user = {
            'authorized': True,
            'email': session['email'],
            'name': session['username']
        }
        print(user)
        return user

    
def is_user_authorized():
    """Simple check"""
    return 'access_token' in session





