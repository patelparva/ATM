from itertools import count
from operator import index
from os import name


class Account(object):
    def __init__(self, name, balance, atm_card_no, atm_PIN):
        self.name=name
        self.balance=balance
        self.atm_card_no=atm_card_no
        self.atm_PIN=atm_PIN
        self.account=[name,balance,atm_card_no,atm_PIN]

    def withDraw(self,amount):
        if amount>self.balance:
            print('Your don\'t have sufficient balance in your bank account')

        else:
            self.balance=self.balance-amount
            print(f'Your withdrawal was successful. You bank balance is {self.balance}')

    def deposit(self, amount):
        self.balance=self.balance+amount
        print(f'Your deposit was successful. Your bank balance is {self.balance}')
        
    def checkBalance(self):
        print(f'Your bank balance is {self.balance}')

def main():
    all_Accounts=[]
    Parva=Account('Parva Patel',2000,62185114,1234)
    all_Accounts.append(Parva.account)
    print(all_Accounts)
    atm_card_no=int(input('Enter Your ATM Card Number. '))
    atm_pin=int(input('Enter Your ATM Pin Number. '))

    index=''
    count=0

    for account in all_Accounts:
        try:
            account.index(atm_card_no)
            index=count
            break
        except:
            count+=1
            break

    if index!='':
        if all_Accounts[index][3]==atm_pin:
            selection=''
            name=all_Accounts[index][0]
            split_name=name.split(' ')
            first_name=split_name[0]
            print(first_name)

            while selection!=4:
                print('1. Check Balance')
                print('2. Deposit')
                print('3. WithDraw')
                print('4. Exit')
                selection=int(input('Select and type in the number from the above given option '))

                if selection==1:
                    first_name.checkBalance()
                elif selection==2:
                    deposit_amount=int(input('Enter The Amount You want to Deposit '))
                    first_name.deposit(deposit_amount)
                elif selection==3:
                    withdraw_amount=int(input('Enter The Amount You want to WithDraw '))
                    first_name.withDraw(withdraw_amount)
                elif selection==4:
                    print('Thank you for choosing our Bank')
                    break
                else:
                    print('Invalid Selection.')
        
        else:
            print('Invalid PIN')
    
    else:
        print('Bank Account does not exist')

if __name__ == '__main__':
    main()
    