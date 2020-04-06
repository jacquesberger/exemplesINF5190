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

from flask import Flask
from flask import g
from flask import jsonify
from flask import render_template
from flask import request
from flask_json_schema import JsonSchema
from flask_json_schema import JsonValidationError
import json

from .database import Database
from .person import Person
from .schemas import person_insert_schema
from .schemas import person_update_schema

app = Flask(__name__, static_url_path="", static_folder="static")
schema = JsonSchema(app)


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


@app.errorhandler(JsonValidationError)
def validation_error(e):
    errors = [validation_error.message for validation_error in e.errors]
    return jsonify({'error': e.message, 'errors': errors}), 400


@app.route('/')
def documentation():
    return render_template('doc.html')


@app.route('/api/person', methods=["POST"])
@schema.validate(person_insert_schema)
def create_person():
    data = request.get_json()
    person = Person(None, data["lastname"], data["firstname"], data["age"])
    person = get_db().save_person(person)
    return jsonify(person.asDictionary()), 201


@app.route('/api/person', methods=["GET"])
def get_persons():
    persons = get_db().read_all_persons()
    return jsonify([person.asDictionary() for person in persons])


@app.route('/api/person/<id>', methods=["GET"])
def get_person(id):
    person = get_db().read_one_person(id)
    if person is None:
        return "", 404
    else:
        return jsonify(person.asDictionary())


@app.route('/api/person/<id>', methods=["PUT"])
@schema.validate(person_update_schema)
def modify_person(id):
    person = get_db().read_one_person(id)
    if person is None:
        return "", 404
    else:
        data = request.get_json()
        person.lastname = data["lastname"]
        person.firstname = data["firstname"]
        person.age = data["age"]
        get_db().save_person(person)
        return jsonify(person.asDictionary())


@app.route('/api/person/<id>', methods=["DELETE"])
def delete_person(id):
    person = get_db().read_one_person(id)
    if person is None:
        return "", 404
    else:
        get_db().delete_person(person)
        return "", 200
