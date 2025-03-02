#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

# gather input from user
answer = str(input('What is the answer to the Great Question of Life, the Universe and Everything? '))

# Trim all spaces from input
answer = answer.strip()

# Force the input to title case.
answer = answer.title()

if '-' in answer:
    answer = answer.lower()

if answer == "42":
    response = "Yes"
elif answer == "Forty Two":
    response = "Yes"
elif answer == "forty-two":
    response = "Yes"
else:
    response = "No"

print(f'{response}')
