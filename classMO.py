
class customer1(object):
    name = 'Harrison'
    pin = 1234
    phoneNumber = '0201234567'
    balance = 5200

    def deposit(self, phoneN):
        self.phoneN = phoneN
        if eval(input('enter pin: ')) == d.pin:
            amount = eval(input('enter amount: '))
            self.balance = self.balance + amount
        else:
            print('incorrect pin.')


    def withdrawal(self,amount):
        amount = eval(input("Enter amount to withdraw: "))
        if amount == self.balance -2:
            print('amount you are withdrawing: ', amount)
            self.balance - amount
        

    def get_balance(self):
        return self.balance

    def transfer (self):
        senderN = input("Sender's Number: ")
        amount  = eval(input('Enter amount to transfer: '))
        if amount == self.balance - 2:
            input('Enter pin to proceed: ' )
            self.balance = self.balance - amount
            d1.balance = d1.balance + amount
        else:
            print("You don't have enough balance for this transaction")
        
    def momoP(self):
        print('Welcome to Python MOMO services. \nMenu')
        choice = eval(input('1) Transfer Money \n2) Deposit Money \n3) Withdraw Money \n4) Get Balance \nEnter: '))
        if choice == 1:
            d.transfer()
        elif choice == 2:
            d.deposit()
        elif choice == 3:
            d.withdrawal()
        elif choice == 4:
            d.get_balance()
        else:
            print('Wrong Entry.')
            start = input('Enter 0 to start again: ')
            d.momoP()

d = customer1()
d1 = customer1()


#d.deposit(12354)
#d.transfer()
d.momoP()


print(d.balance)
print(d1.balance)

        