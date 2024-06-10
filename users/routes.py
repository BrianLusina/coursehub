from .models import db
from flask import Blueprint, request, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

routes = Blueprint('routes', __name__)

# Your Code Here
