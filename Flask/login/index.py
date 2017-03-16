# coding: utf8

# Copyright 2017 Jacques Berger
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import session
from database import Database
import hashlib
import uuid

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.route('/')
def start_page():
    username = None
    if session.has_key("id"):
        username = get_db().get_session(session["id"])
    return render_template('accueil.html', username=username)


@app.route('/confirmation')
def confirmation_page():
    return render_template('confirmation.html')


@app.route('/formulaire', methods=["GET", "POST"])
def formulaire_creation():
    if request.method == "GET":
        return render_template("formulaire.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        # Vérifier que les champs ne sont pas vides
        if username == "" or password == "":
            return render_template("formulaire.html", error="Tous les champs sont obligatoires.")

        # TODO Faire la validation du formulaire
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password + salt).hexdigest()
        db = get_db()
        db.create_user(username, salt, hashed_password)

        return redirect("/confirmation")


@app.route('/login', methods=["POST"])
def log_user():
    username = request.form["username"]
    password = request.form["password"]
    # Vérifier que les champs ne sont pas vides
    if username == "" or password == "":
        return redirect("/")

    user = get_db().get_user_login_info(username)
    if user is None:
      return redirect("/")

    salt = user[0]
    hashed_password = hashlib.sha512(password + salt).hexdigest()
    if hashed_password == user[1]:
        # Accès autorisé
        id_session = uuid.uuid4().hex
        get_db().save_session(id_session, username)
        session["id"] = id_session
        return redirect("/")
    else:
        return redirect("/")

@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect("/")

app.secret_key = "(*&*&322387he738220)(*(*22347657"
