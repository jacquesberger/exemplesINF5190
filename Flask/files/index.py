# Copyright 2018 Jacques Berger
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
from flask import make_response
from flask import g
from flask import request
from flask import redirect
from flask import Response
from .database import Database
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
    return render_template('formulaire.html')


@app.route('/confirmation')
def confirmation_page():
    db = get_db()
    profiles = db.get_profiles()
    return render_template('confirmation.html', profiles=profiles)


@app.route('/formulaire', methods=["POST"])
def formulaire_creation():
    lastname = request.form["nom"]
    firstname = request.form["prenom"]

    # TODO Valider le formulaire et gérer les erreurs

    photo = None
    picture_id = None
    if "photo" in request.files:
        photo = request.files["photo"]
        picture_id = str(uuid.uuid4().hex)

    db = get_db()
    db.create_profile(firstname, lastname, picture_id)
    if picture_id is not None:
        db.create_picture(picture_id, photo)

    return redirect("/confirmation")

@app.route('/image/<pic_id>.png')
def download_picture(pic_id):
    db = get_db()
    binary_data = db.load_picture(pic_id)
    if binary_data is None:
        return Response(status=404)
    else:
        response = make_response(binary_data)
        response.headers.set('Content-Type', 'image/png')
    return response
