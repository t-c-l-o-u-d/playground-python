#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return len_check(s) \
    and first_two_char_check(s) \
    and punctuation_check(s) \
    and zero_check(s) \
    and middle_num_check(s)


def first_two_char_check(plate):
    return plate[:2].isalpha()

def len_check(plate):
    return 2 <= len(plate) <= 6

def punctuation_check(plate):
    punc_list = {"%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"}

    i = len(plate) - 1
    while i != 0:
        if plate[i] in punc_list:
            return False
        i -= 1
    else:
        return True

def zero_check(plate):
    i = 0
    while i != len(plate):
        if plate[i].isdigit() and plate[i] == "0":
            return False
        elif plate[i].isdigit():
            return True
        else:
            i += 1
    else:
        return True

def middle_num_check(plate):
    i = 0
    j = 1
    while i != len(plate) and j != len(plate):
        if plate[i].isdigit() and plate[j].isalpha():
            return False
        else:
            i += 1
            j += 1
    else:
        return True

main()
