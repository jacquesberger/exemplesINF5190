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


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/location.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_pays(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select id, nom from pays")
        pays = cursor.fetchall()
        return [(un_pays[0], un_pays[1]) for un_pays in pays]

    def add_pays(self, nom):
        connection = self.get_connection()
        connection.execute("insert into pays(nom) values(?)", (nom,))
        connection.commit()

    def get_provinces(self, pays_id):
        cursor = self.get_connection().cursor()
        cursor.execute("select id, nom from provinces where pays_id = ?",
                       (pays_id,))
        provinces = cursor.fetchall()
        return [(prov[0], prov[1]) for prov in provinces]

    def get_villes(self, province_id):
        cursor = self.get_connection().cursor()
        cursor.execute("select id, nom from villes where province_id = ?",
                       (province_id,))
        villes = cursor.fetchall()
        return [(une_ville[0], une_ville[1]) for une_ville in villes]
