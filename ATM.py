import pyinputplus as pyip 
from datetime import datetime
import json
import pprint

""" customersDB = {"Shrek":"1234", "Fiona":"5678", "Donkey":"0000"}

with open('clientsDB.json', 'w') as outfile:
    json.dump(customersDB, outfile)   """

with open('clientsDB.json','r') as read_file:
    records = json.load(read_file)
    pprint.pprint(records)
    print()

currentday= datetime.today().strftime('%b %d, %H:%M')
print(currentday)
print()

client = pyip.inputStr('what is your name ? \n').lower().title()
if client in records:
    print()
    print("Welcome {} to E-L Bank \n".format(client))
else:
    print()
    print('invalid ID \n')

attempts = 3

while attempts != 0:
    pin = pyip.inputPassword('kindly enter your pin : \n')
    if records[client]== pin:
        print()
        print('Pin correct! \n')
        break

    else:
        print('incorrect pin')
        attempts -=1

        if attempts == 0 :
            print('Debit card seized due to three failed attempts')
            print('terminating the session, have a nice day')
            exit()

def transaction():
    print()
    print('what transaction do you want to perform ? \n')
    options = pyip.inputMenu(['Deposit', 'Withdrawal', 'Balance Enquiry'],lettered=False, numbered=True)
    if options == 'Deposit':
        print("kindly put the notes in the tray \n\n***Processing*** \n\nDeposit completed \n\n")
        print("Do you want to perform other transactions ?\n")
        done=pyip.inputMenu(["Yes","No"],lettered=False,numbered=True)
        if done == 'No':
        pass
    if options == 'Withdrawal':
        print("how much would you like to witdraw ?(in multiples of 10)\n\n")
        cashout = pyip.inputInt('enter amount: ')
        print('€{} dispensed, have a nice day {}'.format(cashout,client))
        print("Do you want to perform other transactions ?\n")
        done=pyip.inputMenu(["Yes","No"],lettered=False,numbered=True)
        if done == 'No':
        pass
    if options == 'Balance Enquiry':
        print('Current Account - €1980\nSavings Account - €50,000')
        print("Do you want to perform other transactions ?\n")
        done=pyip.inputMenu(["Yes","No"],lettered=False,numbered=True)
        if done == 'No':
        pass
    else:
        transaction()
transaction()

print("thanks for banking with us {}\n".format(client))    
        



