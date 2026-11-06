from flask import Blueprint, render_template

my_arts_bp = Blueprint("myArts", __name__)

@my_arts_bp.route("/myArts")
def arts():
    return render_template("arts.html")