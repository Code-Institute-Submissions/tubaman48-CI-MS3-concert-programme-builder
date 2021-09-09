import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_progs")
def get_progs():
    progs = list(mongo.db.progs.find())
    return render_template("progs.html", progs=progs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/prog_add", methods=["GET", "POST"])
def prog_add():
    if request.method == "POST":
        is_finalised = True if request.form.get("is_finalised") else False
        prog = {
            "concert_venue": request.form.get("concert_venue"),
            "concert_date": request.form.get("concert_date"),
            "concert_times": request.form.get("concert_times"),
            "band_name": request.form.get("band_name"),
            "prog_item": request.form.getlist("prog_item"),
            "is_finalised": is_finalised,
            "created_by": session["user"]
        }
        mongo.db.progs.insert_one(prog)
        flash("Concert Programme Successfully Added")
        return redirect(url_for("get_progs"))

    venues = mongo.db.venues.find().sort("venue_name", 1)
    bands = mongo.db.bands.find().sort("band_name", 1)
    music_items = mongo.db.music_items.find().sort("genre_name"+"title", 1)
    return render_template(
        "prog_add.html", venues=venues, bands=bands, music_items=music_items)


@app.route("/prog_edit/<prog_id>", methods=["GET", "POST"])
def prog_edit(prog_id):
    if request.method == "POST":
        is_finalised = True if request.form.get("is_finalised") else False
        submit = {
            "concert_venue": request.form.get("concert_venue"),
            "concert_date": request.form.get("concert_date"),
            "concert_times": request.form.get("concert_times"),
            "band_name": request.form.get("band_name"),
            "prog_item": request.form.getlist("prog_item"),
            "is_finalised": is_finalised,
            "created_by": session["user"]
        }
        mongo.db.progs.update({"_id": ObjectId(prog_id)}, submit)
        flash("Concert Programme Successfully Updated")

    prog = mongo.db.progs.find_one({"_id": ObjectId(prog_id)})
    venues = mongo.db.venues.find().sort("venue_name", 1)
    bands = mongo.db.bands.find().sort("band_name", 1)
    music_items = mongo.db.music_items.find().sort("genre_name"+"title", 1)
    return render_template(
        "prog_edit.html",
        prog=prog, venues=venues, bands=bands, music_items=music_items)


@app.route("/prog_delete/<prog_id>")
def prog_delete(prog_id):
    mongo.db.progs.remove({"_id": ObjectId(prog_id)})
    flash("Concert Programme Successfully Deleted")
    return redirect(url_for("get_progs"))


@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
