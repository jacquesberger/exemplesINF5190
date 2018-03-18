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
from .database import Database

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
    return render_template('accueil.html')


@app.route('/liste')
def show_list():
    artists = get_db().get_artists()
    return render_template('artistes.html', artist_names=artists)


@app.route('/deux-listes')
def show_two_lists():
    artists = get_db().get_artists()
    albums = get_db().get_albums()
    return render_template('2listes.html', artists=artists, albums=albums)


@app.route('/vide')
def show_two_empty_lists():
    artists = []
    albums = []
    return render_template('2listes-vides.html',
                           artists=artists, albums=albums)


@app.route('/formulaire')
def show_form():
    return render_template('form.html')


@app.route('/new', methods=['POST'])
def post_form():
    name = request.form['nom']
    if len(name) == 0:
        return render_template('form.html', erreur='Le nom est obligatoire')
    else:
        get_db().insert_artist(name)
        return redirect('/liste')
