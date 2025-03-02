#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

camel = input('camelCase: ')
snake = ""

for letter in camel:
    if letter.isupper():
        snake = snake + "_" + letter.lower()
    else:
        snake = snake + letter

print(f'snake_case: {snake}')
