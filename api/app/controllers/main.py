from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..config.database import db
from ..models import user

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def index():

    return "fgrgrgg"
