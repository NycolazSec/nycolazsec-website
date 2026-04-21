from flask import Blueprint, render_template, request, redirect, url_for

index = Blueprint('index', __name__)

name = "NycolazSec"

@index.route('/')
def home():
    return render_template('index.html', name=name)