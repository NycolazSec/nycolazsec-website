from flask import Blueprint, render_template, request, redirect, url_for

profile = Blueprint('profile', __name__)

@profile.route('/profile')
def profile_home():
    return render_template('profile.html')


