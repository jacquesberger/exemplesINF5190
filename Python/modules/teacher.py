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


class Teacher(Person):
    def __init__(self, firstname, lastname, age, employee_number):
        super(Teacher, self).__init__(firstname, lastname, age)
        self.employee_number = employee_number

    def get_complete_name(self):
        return "A Teacher Has No Name"
