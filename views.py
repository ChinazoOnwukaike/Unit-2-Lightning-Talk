from flask import Blueprint

dog_bp = Blueprint("dog", __name__)

@dog_bp.route("/", methods=["GET"])
def home():
    return "<h1>Hello World</h1>"