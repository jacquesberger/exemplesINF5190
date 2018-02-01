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


import sqlite3


def build_artist_dictionary(row):
    return {"id": row[0], "nom": row[1], "est_solo": row[2],
            "nombre_individus": row[3]}


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/musique.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_artists(self):
        cursor = self.get_connection().cursor()
        cursor.execute(("select id, nom, est_solo,"
                        " nombre_individus from artiste"))
        artists = cursor.fetchall()
        return [build_artist_dictionary(each) for each in artists]

    def get_artist(self, identifier):
        cursor = self.get_connection().cursor()
        cursor.execute(("select id, nom, est_solo, nombre_individus "
                        "from artiste where id = ?"), (identifier,))
        artist = cursor.fetchone()
        if artist is None:
            return None
        else:
            return build_artist_dictionary(artist)
