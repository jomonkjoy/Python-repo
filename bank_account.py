import filestore
import time
import datetime

WELCOME_MESSAGE = "Welcome to PostBank, We care for you" + "\n"
def postbank():
    print (WELCOME_MESSAGE)
    prompts = {
        1: BankAccount,   # Creates a new customer profile
        2: ReturnCustomer # Checks for existing customer
    }
    while True:
        prompt = int(raw_input("To open a new bank account, Press 1" + "\n"
                             + "To access your existing account & transact press 2:" + "\n"))
        if prompt in prompts:
            prompts[prompt]()
        else:
            print "You have pressed the wrong key, please try again"


# Class for creating an instance of a new back account and other default bank functions
class BankAccount:
    def __init__(self):
        ##calls functions in the module filestore
        self.user_name
        self.user_password
        self.balance = filestore.cus_account_check()
        print ("Thank you {username}, your account is set up and ready to use,".format(username=self.username)
            + "\n" + "a 100 pounds has been credited to your account")
        self.user_functions()


    def user_functions(self):
        print("\n\nTo access any function below, enter the corresponding key")
        print ("To:" + "\n"
            + "Check Balance, press B" + "\n"
            + "Deposit cash:  press D" + "\n"
            + "Withdraw cash, press W" + "\n"
            + "Delete account press X" + "\n"
            + "Exit service,  press E" + "\n")

        functions = {
            'b': self.check_balance,
            'd': self.deposit_cash,
            'w': self.withdraw_cash,
        }
        while True:
            answer = raw_input("> ").lower()
            if answer in functions:
                ##passcheck function confirms stored password with user input
                self.pass_check()
                functions[answer]()
            elif answer is 'x':
                print ("{username}, your account is being deleted".format(username=self.username))
                file_store.delete_account(self.username)
                print ("Your account has been successfuly deleted, Goodbye.")
            elif answer is 'e':
                print ("Thank you for using Dot Inc Bank Services")
                print ("Goodbye {username}".format(username=self.username))
                exit()
            else:
                print "No function assigned to this key, please try again"

    def check_balance(self):
        date = datetime.date.today().strftime('%d-%B-%Y')
        print ("Your account balance as at {time} is {balance}").format(time=date, balance=self.balance)
        self.transact_again()

    def withdraw_cash(self):
        amount = float(raw_input("Please enter amount to withdraw:" + "\n"))
        self.balance -= amount
        print ("Your new account balance is {balance}".format(balance=self.balance) + "\n")
        file_store.balance_update(self.username, -amount)
        self.transact_again()

    def deposit_cash(self):
        amount = float(raw_input("Please enter amount to deposit:" + "\n"))
        self.balance += amount
        print ("Your new account balance is {balance}".format(balance=self.balance) + "\n")
        file_store.balance_update(self.username, -amount)
        self.transact_again()



    def transact_again(self):
        while True:
            answer = raw_input("Do you want to do another transaction? (y/n)" + "\n").lower()
            if ans is 'y':
                self.user_functions()
            elif ans is 'n':
                print ("Thank you for using PostBank we value you. Have a good day.")
                print ("Goodbye {username}").format(username=self.username)
                exit()
            elif ans is not in ['y', 'n']:
                print "Unknown key pressed, please choose either 'N' or 'Y'"


    def pass_check(self):
        # Prompts user for password with every transaction and counterchecks it with stored passwords"
        attempts = 3
        while attempts > 0:
            answer = raw_input("Please type in your password to continue with the transaction:" + "\n")
            if answer is self.user_password:
                return True
            else:
                print "That is the wrong password"
                attempts -= 1
                print ("{attempts} more attempt(s) remaining".format(attempts=attempts))

        print ("Account has been frozen due to three wrong password attempts," + "\n"
            + "Contact your bank for help.")
        exit()


class ReturnCustomer():
    def __init__(self):
        self.username
        self.user_password
        self.balance = file_store.old_customer_check()
        self.user_functions()

postbank()
