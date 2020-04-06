# Copyright 2020 Jacques Berger
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
            self.connection = sqlite3.connect('db/person.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    # def get_personnes(self):
        # cursor = self.get_connection().cursor()
        # cursor.execute("select id, nom, prenom from personne")
        # personnes = cursor.fetchall()
        # return [(un_pays[0], un_pays[1]) for un_pays in pays]

    def save_person(self, person):
        connection = self.get_connection()
        connection.execute("insert into person(lastname, firstname, age) values(?, ?, ?)", (person.lastname, person.firstname, person.age))
        connection.commit()

        cursor = connection.cursor()
        cursor.execute("select last_insert_rowid()")
        result = cursor.fetchall()
        person.id = result[0][0]
        return person
