#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

response = input('Greeting: ')
response = response.strip()
response = response.lower()

if response.startswith('hello'):
    payment = "$0"
elif response.startswith('h') and not response.startswith('hello'):
    payment = "$20"
else:
    payment = "$100"

print(f'{payment}')
