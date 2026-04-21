from flask import Blueprint, render_template

projects = Blueprint('projects', __name__)

@projects.route('/projects')
def projects_home():
    return render_template('projects.html')