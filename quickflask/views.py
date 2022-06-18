from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Matty")


@views.route("/profile")
def profile():
    name = request.args.get('name') or "Jim"
    return render_template("index.html", name=name)


@views.route("/json")
def test_json():
    return jsonify({"username": "Matty!", "age": 31})


@views.route("/go-to-json")
def redirect_tojson():
    return redirect(url_for("views.test_json"))

