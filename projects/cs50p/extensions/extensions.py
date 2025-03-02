#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

import mimetypes

response = input('File name: ')

response = response.strip()

file_type, file_encoding = mimetypes.guess_type(response)

if file_type is None:
    file_type = "application/octet-stream"

print(f'{file_type}')
