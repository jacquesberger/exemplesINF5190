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
from flask import make_response
from flask import request
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
    artists = get_db().get_artists()
    last_id = request.cookies.get('last')
    last_artist = None
    if last_id is not None:
        last_artist = get_db().get_artist(last_id)

    return render_template('accueil.html', artists=artists, last=last_artist)


@app.route('/artiste/<identifier>')
def artist_page(identifier):
    artist = get_db().get_artist(identifier)
    if artist is None:
        return render_template('404.html'), 404
    else:
        response = make_response(render_template('artiste.html',
                                                 artist=artist))
        response.set_cookie("last", identifier)
        return response
