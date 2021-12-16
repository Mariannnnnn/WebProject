from flask import Blueprint, render_template,redirect,url_for

views = Blueprint(__name__, "views")

@views.route("/")
def main():
    return render_template("index.html")

@views.route("/future.html")
def future():
    return render_template("future.html")

@views.route("/technology.html")
def technology():
    return render_template("technology.html")

@views.route("/universe.html")
def universer():
    return render_template("universe.html")

@views.route("/kardashev.html")
def kardashev():
    return render_template("kardashev.html")

@views.route("/dark.html")
def dark():
    return render_template("dark.html")

@views.route("/comment.html")
def comment():
    return render_template("comment.html")

@views.route("/admin")
def admin():
    return render_template("admin.html")




