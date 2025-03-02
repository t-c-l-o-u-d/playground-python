#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

def main():
    time = input('What time is it? ')
    time = convert(time)
    if 7.0 <= time <= 8.0:
        time = "breakfast time"
    elif 12.0 <= time <= 13.0:
        time = "lunch time"
    elif 18.0 <= time <= 19.0:
        time = "dinner time"

    print(f'{time}')


def convert(time):
    if " " in time:
        time, convention = time.split(" ")
    else:
        convention = ""

    hours, minutes = time.split(":")

    if convention:
        if 'p' in convention:
            hours = float(hours) + 12

    minutes = float(minutes) / 60
    time = float(hours) + float(minutes)
    return time


if __name__ == "__main__":
    main()
