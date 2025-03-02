#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    d = float(d.replace('$', ''))
    return d


def percent_to_float(p: str) -> float:
    p = float(p.replace('%', ''))
    p = p / 100
    return p


main()
