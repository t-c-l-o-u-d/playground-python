#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

user_input = input('Input: ')
program_output = ""

for letter in user_input:
    if letter.lower() not in {"a", "e", "i", "o", "u"}:
        program_output = program_output + letter

print(f'Output: {program_output}')
