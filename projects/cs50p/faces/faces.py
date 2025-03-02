#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

def convert(input: str) -> str:
    input = input.replace(':)', '\U0001F642')
    input = input.replace(':(', '\U0001F641')
    return input


def main():
    response = str(input(''))
    response = convert(response)
    print(response)


main()
