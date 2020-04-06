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
from .person import Person


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

    def read_all_persons(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select rowid, lastname, firstname, age from person")
        persons = cursor.fetchall()
        return [Person(one_person[0], one_person[1], one_person[2],
                       one_person[3]) for one_person in persons]

    def read_one_person(self, id):
        cursor = self.get_connection().cursor()
        cursor.execute("select rowid, lastname, firstname, "
                       "age from person where rowid = ?", (id,))
        persons = cursor.fetchall()
        if len(persons) is 0:
            return None
        else:
            person = persons[0]
            return Person(person[0], person[1], person[2], person[3])

    def save_person(self, person):
        connection = self.get_connection()
        if person.id is None:
            connection.execute("insert into person(lastname, firstname, age) "
                               "values(?, ?, ?)",
                               (person.lastname, person.firstname, person.age))
            connection.commit()

            cursor = connection.cursor()
            cursor.execute("select last_insert_rowid()")
            result = cursor.fetchall()
            person.id = result[0][0]
        else:
            connection.execute("update person set lastname = ?, firstname = ?,"
                               "age = ? where rowid = ?",
                               (person.lastname, person.firstname, person.age,
                                person.id))
            connection.commit()
        return person

    def delete_person(self, person):
        connection = self.get_connection()
        connection.execute("delete from person where rowid = ?", (person.id,))
        connection.commit()
