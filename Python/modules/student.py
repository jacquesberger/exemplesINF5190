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


class Student(Person):
    def __init__(self, firstname, lastname, age, code):
        super(Student, self).__init__(firstname, lastname, age)
        self.code = code

    def get_complete_name(self):
        return "%s [%s]" % (super(Student, self).get_complete_name(),
                            self.code)
