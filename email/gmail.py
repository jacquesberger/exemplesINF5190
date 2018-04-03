# coding: utf8

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

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

source_address = "source.name@gmail.com"
destination_address = "destination@gmail.com"
body = "Please note that I'm writing a script to send emails."
subject = "I send mails!"

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = source_address
msg['To'] = destination_address

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(source_address, "secret123")
text = msg.as_string()
server.sendmail(source_address, destination_address, text)
server.quit()
