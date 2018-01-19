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

from person import Person
from student import Student
from teacher import Teacher

regular_person = Person("Vince", "Neil", 51)
print(regular_person.get_complete_name())

steven = Student("Steven", "Stevenson", 19, "STES12129701")
print(steven.get_complete_name())

teacher = Teacher("Jacques", "Berger", 87, "IEPSW3")
print(teacher.get_complete_name())
