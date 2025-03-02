#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

x, y, z = input('Expression: ').split(" ")

if y == "+":
    result = float(x) + float(z)
elif y == "-":
    result = float(x) - float(z)
elif y == "*":
    result = float(x) * float(z)
elif y == "/":
    result = float(x) / float(z)


print(f'{result}')
