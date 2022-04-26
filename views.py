from flask import Blueprint, render_template

dog_bp = Blueprint("dog", __name__)

@dog_bp.route("/", methods=["GET"])
def home():
    return render_template('home.html')