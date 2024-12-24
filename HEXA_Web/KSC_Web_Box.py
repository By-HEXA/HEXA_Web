from flask import Flask, request, render_template, redirect, url_for, flash, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

Box = Blueprint('Box', __name__)

@Box.route('/gallery')
def gallery():
    return render_template('gallery.html')
