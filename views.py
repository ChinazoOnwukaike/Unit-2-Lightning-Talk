from flask import Blueprint

dog_bp = Blueprint("dog", __name__)

@dog_bp.route("/", methods=["GET"])
def home():
    return "Hello World"