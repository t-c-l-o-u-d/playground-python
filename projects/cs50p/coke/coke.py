#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

balance = 50

while balance > 0:
    print(f'Amount Due: {balance}')

    coin = int(input('Insert Coin: '))
    while coin not in (5, 10, 25):
        print(f'Amount Due: {balance}')
        coin = int(input('Insert Coin: '))
    else:
        balance = balance - coin


else:
    print(f'Change Owed: {balance * -1}')
