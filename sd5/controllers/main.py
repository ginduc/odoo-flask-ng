from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required

from sd5.extensions import cache
from sd5.forms import LoginForm, RecipientForm
from sd5.models import User

import logging
log = logging.getLogger('werkzeug')

main = Blueprint('main', __name__)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        flash("Logged in successfully.", "success")
        return redirect(request.args.get("next") or url_for(".home"))

    return render_template("login.html", form=form)


@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")

    return redirect(url_for(".home"))


@main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200


# ======================================================
# Sender
# ======================================================
@main.route("/sender/search")
def search_sender():
    keyword = request.args.get('keyword')

    if keyword is None:
        flash("Search keywords must have at least three (3) characters",
              "warning")
    else:
        if len(keyword) < 3:
            flash("Search keywords must have at least three (3) characters",
                  "warning")

    # data = searchByKeyword(keyword)
    data = []

    return render_template("sender_search.html", data=data)


# ======================================================
# Recipient
# ======================================================
@main.route("/recipient/new", methods=["GET", "POST"])
def new_recipient():
    form = RecipientForm()

    if form.validate_on_submit():
        recipient = form.to_model()
        log.info("recipient: " + str(recipient))

        flash("Recipient was successfully saved!", "success")

    return render_template("recipient_form.html", form=form)
