""" Application function definitions and routing """

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
from flask import jsonify, json
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("MS3_SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_progs")
def get_progs():
    """
    Function to display a list of all concert programmes.
    """
    progs = list(mongo.db.progs.find())
    return render_template("progs.html", progs=progs)


# <-- User Management -->
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function for allowing new members to register on the site.
    Also checks if the username is already registered on the site.
    Existing members can also follow the link to log in from this page.
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register_new = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register_new)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Function for logging in existing users.
    New users can follow the link to register a new account from here.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
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
    """
    Function to show user profile details (if user is logged in).
    """
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        progs = list(mongo.db.progs.find({'created_by': session["user"]}))
        return render_template("profile.html", username=username, progs=progs)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Function to allow users to logout of the site.
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# <-- Concert Programme Management -->
@app.route("/prog_add", methods=["GET", "POST"])
def prog_add():
    """
    Registered users can create a new concert programme from this page.
    The drop down menu allows existing pieces to be selected for the programme.
    """
    if request.method == "POST":
        is_finalised = True if request.form.get("is_finalised") else False
        prog = {
            "concert_venue": request.form.get("concert_venue"),
            "concert_date": request.form.get("concert_date"),
            "concert_times": request.form.get("concert_times"),
            "band_name": request.form.get("band_name"),
            "prog_items": request.form.getlist("music_items_selector"),
            "is_finalised": is_finalised,
            "created_by": session["user"]
        }
        mongo.db.progs.insert_one(prog)
        flash("Concert Programme Successfully Added")
        return redirect(url_for("get_progs"))

    venues = mongo.db.venues.find().sort("venue_name", 1)
    bands = mongo.db.bands.find().sort("band_name", 1)
    music_items = mongo.db.music_items.find().sort("genre_name"+"title", 1)
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template(
        "prog_add.html",
        venues=venues, bands=bands, music_items=music_items, genres=genres)


@app.route("/prog_edit/<prog_id>", methods=["GET", "POST"])
def prog_edit(prog_id):
    """
    Registered users can edit concert programmes from this page if they
    created the orginal programme
    (also actionable by the Librarian admin user).
    The drop down menu allows existing pieces to be selected for the programme.
    """
    if request.method == "POST":
        is_finalised = True if request.form.get("is_finalised") else False
        submit = {
            "concert_venue": request.form.get("concert_venue"),
            "concert_date": request.form.get("concert_date"),
            "concert_times": request.form.get("concert_times"),
            "band_name": request.form.get("band_name"),
            "prog_items": request.form.getlist("music_items_selector"),
            "is_finalised": is_finalised,
            "created_by": session["user"]
        }
        mongo.db.progs.update({"_id": ObjectId(prog_id)}, submit)
        flash("Concert Programme Successfully Updated")
        return redirect(url_for("get_progs"))

    prog = mongo.db.progs.find_one({"_id": ObjectId(prog_id)})
    venues = mongo.db.venues.find().sort("venue_name", 1)
    bands = mongo.db.bands.find().sort("band_name", 1)
    music_items = mongo.db.music_items.find().sort("genre_name"+"title", 1)
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template(
        "prog_edit.html",
        prog=prog, venues=venues, bands=bands, music_items=music_items,
        genres=genres)


@app.route("/prog_delete/<prog_id>")
def prog_delete(prog_id):
    """
    Registered users can remove concert programmes if they created the
    orginal programme (also actionable by the Librarian admin user).
    Once deleted the user will be returned to the concert programme listing.
    """
    mongo.db.progs.remove({"_id": ObjectId(prog_id)})
    flash("Concert Programme Successfully Deleted")
    return redirect(url_for("get_progs"))


# <-- Genre Management -->
@app.route("/get_genres")
def get_genres():
    """
    Librarian admin function to list existing genres for maintenance.
    Add new genre function also available from here.
    """
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/genre_add", methods=["GET", "POST"])
def genre_add():
    """
    Librarian admin function to add a new genre.
    """
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("genre_add.html")


@app.route("/genre_edit/<genre_id>", methods=["GET", "POST"])
def genre_edit(genre_id):
    """
    Librarian admin function to edit an existing genre.
    """
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("genre_edit.html", genre=genre)


@app.route("/genre_delete/<genre_id>")
def genre_delete(genre_id):
    """
    Librarian admin function to remove an existing genre.
    """
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


# <-- Venue Management -->
@app.route("/get_venues")
def get_venues():
    """
    Librarian admin function to list existing venues for maintenance.
    Add new venue function also available from here.
    """
    venues = list(mongo.db.venues.find().sort("venue_name", 1))
    return render_template("venues.html", venues=venues)


@app.route("/venue_add", methods=["GET", "POST"])
def venue_add():
    """
    Librarian admin function to add a new venue.
    """
    if request.method == "POST":
        venue = {
            "venue_name": request.form.get("venue_name")
        }
        mongo.db.venues.insert_one(venue)
        flash("New Venue Added")
        return redirect(url_for("get_venues"))

    return render_template("venue_add.html")


@app.route("/venue_edit/<venue_id>", methods=["GET", "POST"])
def venue_edit(venue_id):
    """
    Librarian admin function to edit an existing venue.
    """
    if request.method == "POST":
        submit = {
            "venue_name": request.form.get("venue_name")
        }
        mongo.db.venues.update({"_id": ObjectId(venue_id)}, submit)
        flash("Venue Successfully Updated")
        return redirect(url_for("get_venues"))

    venue = mongo.db.venues.find_one({"_id": ObjectId(venue_id)})
    return render_template("venue_edit.html", venue=venue)


@app.route("/venue_delete/<venue_id>")
def venue_delete(venue_id):
    """
    Librarian admin function to remove an existing venue.
    """
    mongo.db.venues.remove({"_id": ObjectId(venue_id)})
    flash("Venue Successfully Deleted")
    return redirect(url_for("get_venues"))


# <-- Piece (Music Items) Management -->
@app.route("/get_pieces")
def get_pieces():
    """
    Function to list pieces.
    """
    pieces = list(mongo.db.music_items.find().sort(
        [("genre_name", 1), ("title", 1)]))
    return render_template("pieces.html", pieces=pieces)


@app.route("/search_pieces", methods=["GET", "POST"])
def search_pieces():
    """
    Function to search for pieces.
    """
    query = request.form.get("query")
    pieces = list(mongo.db.music_items.find({"$text": {"$search": query}}))
    return render_template("pieces.html", pieces=pieces)


@app.route("/piece_add", methods=["GET", "POST"])
def piece_add():
    """
    Librarian admin function to add a new piece.
    """
    if request.method == "POST":
        piece = {
            "genre_name": request.form.get("genre_name"),
            "title": request.form.get("title"),
            "composer": request.form.get("composer"),
            "arranger": request.form.get("arranger"),
            "status": request.form.get("status"),
            "created_by": session["user"]
        }
        mongo.db.music_items.insert_one(piece)
        flash("New Piece Added")
        return redirect(url_for("get_pieces"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    statuses = mongo.db.statuses.find().sort("status_type", 1)
    return render_template(
        "piece_add.html", genres=genres, statuses=statuses)


@app.route("/piece_edit/<piece_id>", methods=["GET", "POST"])
def piece_edit(piece_id):
    """
    Librarian admin function to edit an existing piece.
    """
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name"),
            "title": request.form.get("title"),
            "composer": request.form.get("composer"),
            "arranger": request.form.get("arranger"),
            "status": request.form.get("status"),
            "created_by": session["user"]
        }
        mongo.db.music_items.update({"_id": ObjectId(piece_id)}, submit)
        flash("Piece Successfully Updated")
        return redirect(url_for("get_pieces"))

    piece = mongo.db.music_items.find_one({"_id": ObjectId(piece_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    statuses = mongo.db.statuses.find().sort("status_type", 1)
    return render_template(
        "piece_edit.html", piece=piece, genres=genres, statuses=statuses)


@app.route("/piece_delete/<piece_id>")
def piece_delete(piece_id):
    """
    Librarian admin function to remove an existing piece.
    Once removed the user will be routed back the pieces summary page.
    """
    mongo.db.music_items.remove({"_id": ObjectId(piece_id)})
    flash("Piece Successfully Deleted")
    return redirect(url_for("get_pieces"))


@app.route("/music_item/<genre_name>", methods=["GET"])
def get_music_items(genre_name):
    """
    Function to enable selection of genre from a list within the prog_add or
    prog_edit functions.
    """
    if genre_name == "All-Genres":
        # Grab all music items regardless of genre
        music_items = list(mongo.db.music_items.find(
        ).sort([
            ("genre_name", 1), ("title", 1)]))
    else:
        # Grab music items just for a particular genre
        music_items = list(mongo.db.music_items.find(
            {"genre_name": genre_name}))

    data = {'music_items': json.loads(json_util.dumps(music_items))}
    return jsonify(data), 200


# <-- HTTP error pages -->
# https://flask.palletsprojects.com/en/2.0.x/errorhandling/
@app.errorhandler(400)
def server_error(error):
    """
    Renders a custom 400 error page with a link
    to take the user back to progs.html
    """
    return render_template('400.html', error=error), 400


@app.errorhandler(401)
def bad_request(error):
    """
    Renders a custom 401 error page with a link
    to take the user back to progs.html
    """
    return render_template('401.html', error=error), 401


@app.errorhandler(403)
def forbidden(error):
    """
    Renders a custom 403 error page with a link
    to take the user back to progs.html
    """
    return render_template('403.html', error=error), 403


@app.errorhandler(404)
def page_not_found(error):
    """
    Renders a custom 404 error page with a link
    to take the user back to progs.html
    """
    return render_template('404.html', error=error), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """
    Renders a custom 405 error page with a link
    to take the user back to progs.html
    """
    return render_template('405.html', error=error), 405


@app.errorhandler(500)
def internal_server_error(error):
    """
    Renders a custom 500 error page with a link
    to take the user back to progs.html
    """
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
