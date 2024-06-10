from flask import Blueprint, render_template, redirect, url_for, flash
from users import routes as userRoutes
from course import routes as courseRoutes
import json
main = Blueprint('main', __name__)

# Your Code Here