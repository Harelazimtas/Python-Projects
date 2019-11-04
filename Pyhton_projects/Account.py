from tkinter import *
import datetime

#single account in bank
class account:
    def __init__(self, name, numberAccount, balance):
        self.name = name
        #is uniqe
        self.numberAccount = numberAccount
        self.balance = balance
        self.Line_of_credit = -1500

    def depositOne(self, sumOfDeposit):
        self.balance += sumOfDeposit

    def pullOne(self, sumOfPull):
        if(self.balance-sumOfPull <self.Line_of_credit):
            return False
        else:
            self.balance = self.balance - sumOfPull
        return True


    def present(self):
        print("the balance is ", self.balance)

#method of decorate
def dateDecorate(f):
    def inner(*args,**kwargs):
        try:
            if f(*args,**kwargs) is True:
                dateLabel.config(text=str(datetime.datetime.now()))
            else:
                dateLabel.config(text="")
        except NameError:
            print("well, it WASN'T defined after all!")

    return inner


#this is the bank
class allAccount:

    def __init__(self):
        self.listOfAccount = []
        self._my = self.myGenerator()


    def add(self, account):
        for i in self.listOfAccount:
            # is uniqe number account
            if i.numberAccount is account.numberAccount:
                return False
        self.listOfAccount.append(account)
        return True

    @dateDecorate
    def deposit(self):
        if (entryOfcurrentAccount.get() is ""):
            errorLabel.config(text="please insert account")
            return False
        if (entryOfMoney.get() is ""):
            errorLabel.config(text="please insert money to deposit")
            return False
        numAccount = int(entryOfcurrentAccount.get())
        money = int(entryOfMoney.get())
        for i in self.listOfAccount:
            if i.numberAccount == numAccount:
                i.depositOne(money)
                errorLabel.config(text="")
                return True
        errorLabel.config(text="account dont find")
        return False

    @dateDecorate
    def balance(self):
        if (entryOfcurrentAccount.get() is ""):
            errorLabel.config(text="please insert your account number")
            return False
        numAccount = int(entryOfcurrentAccount.get())
        for i in self.listOfAccount:
            if i.numberAccount == numAccount:
                str1 = str(i.balance)
                balance1.config(text=str1)
                nameCustomer1.config(text=i.name)
                numberAccount1.config(text=str(i.numberAccount))
                Line_of_credit1.config(text=i.Line_of_credit)
                errorLabel.config(text="")
                return True
        errorLabel.config(text="account dont find")
        return False

    @dateDecorate
    def transferMoney(self):
        if (entryOfcurrentAccount.get() is ""):
            errorLabel.config(text="please insert your account")
            return False
        if (entryOfMoney.get() is ""):
            errorLabel.config(text="please insert money to transfer")
            return False
        if (entryOfOtherAccount.get() is ""):
            errorLabel.config(text="please insert number account to deliver money")
            return False
        numAccount = int(entryOfcurrentAccount.get())
        money = int(entryOfMoney.get())
        numOtherAccount = int(entryOfOtherAccount.get())
        for i in self.listOfAccount:
            if i.numberAccount == numAccount:
                for j in self.listOfAccount:
                    if j.numberAccount == numOtherAccount:
                        true = i.pullOne(money)
                        if true == 1:
                            j.depositOne(money)
                            errorLabel.config(text="")
                            return True
                        else:
                            errorLabel.config(text="can't transfer money")
                            return False
        errorLabel.config(text="can't transfer money")
        return False

    @dateDecorate
    def pull(self):
        if(entryOfcurrentAccount.get() is  ""):
            errorLabel.config(text="please insert account")
            return False
        if(entryOfMoney.get() is ""):
            errorLabel.config(text="please insert money to pull")
            return False
        numAccount = int(entryOfcurrentAccount.get())
        money = int(entryOfMoney.get())
        for i in self.listOfAccount:
            if i.numberAccount == numAccount:
                if i.pullOne(money) is True:
                    errorLabel.config(text="")
                    return True
        errorLabel.config(text="account dont find")
        return False


    def myGenerator(self):
        for i in self.listOfAccount:
            yield (i.balance)


    def show_balance(self):
        try:
            generatorBalance.config(text=str(self._my.__next__()))
            errorLabel.config(text="")
        except StopIteration:
            errorLabel.config(text="end of accounts in bank by generator")
            self._my = self.myGenerator()



if __name__ == "__main__":
    Accounts = allAccount()
    root = Tk()
    #frame
    frameBuuton= Frame(root, bd="30")
    frameBuuton.pack(side=BOTTOM)
    labelFrame = Frame(root, bd="30")
    labelFrame.pack(side=TOP)
    dataFrame = Frame(root, bd="30")
    dataFrame.pack(side=LEFT)
    generatorFrame = Frame(root, bd="30")
    generatorFrame.pack(side=RIGHT)
    #label
    nameCustomer = Label(labelFrame, text="account")
    nameCustomer.grid(row=0, column=0)
    numberAccount = Label(labelFrame, text="numberAccount")
    numberAccount.grid(row=0, column=2)
    balance = Label(labelFrame, text="balance")
    balance.grid(row=0, column=4)
    Line_of_credit = Label(labelFrame, text="Line of credit")
    Line_of_credit.grid(row=0, column=6)
    nameCustomer1 = Label(labelFrame, text="")
    nameCustomer1.grid(row=1, column=0)
    numberAccount1 = Label(labelFrame, text="")
    numberAccount1.grid(row=1, column=2)
    balance1 = Label(labelFrame, text="")
    balance1.grid(row=1, column=4)
    Line_of_credit1 = Label(labelFrame, text="")
    Line_of_credit1.grid(row=1, column=6)
    errorLabel = Label(labelFrame, text="", fg="red")
    errorLabel.grid(row=2, column=0)
    dateLabel = Label(labelFrame, text="", fg="blue")
    dateLabel.grid(row=3, column=0)
    #entry
    Label(dataFrame, text="my account number").grid(row=0, column=0)
    Label(dataFrame, text="money").grid(row=2, column=0)
    Label(dataFrame, text="other account number").grid(row=4, column=0)
    entryOfcurrentAccount = Entry(dataFrame, text="myAccount")
    entryOfcurrentAccount.grid(row=1, column=0)
    entryOfMoney = Entry(dataFrame, text="money")
    entryOfMoney.grid(row=3, column=0)
    entryOfOtherAccount = Entry(dataFrame, text="otherAccount")
    entryOfOtherAccount.grid(row=5, column=0)
    #generator
    Label(generatorFrame, text="balance :").grid(row=0, column=0)
    generatorBalance = Label(generatorFrame, text="")
    generatorBalance.grid(row=0, column=1)
    generatorButton = Button(generatorFrame, text="generator", command=Accounts.show_balance)
    generatorButton.grid(row=1, column=1)
    # button here
    depositButton = Button(frameBuuton, text="deposit", command=Accounts.deposit)
    pullButton = Button(frameBuuton, text="pull", command=Accounts.pull)
    balanceButton = Button(frameBuuton, text="balance/veiw", command=Accounts.balance)
    transferButton = Button(frameBuuton, text="transfer between account", command=Accounts.transferMoney)
    depositButton.grid(row=0, column=1)
    pullButton.grid(row=0, column=3)
    balanceButton.grid(row=0, column=5)
    transferButton.grid(row=0, column=7)
    #add here account to bank only three insert because avi and harel have same account number
    one = account("harel", 1, 1500)
    two = account("guy", 2, 20)
    three = account("asaf", 3, 30)
    four = account("avi", 1, 2000)
    listAccount = [one, two, three, four]
    for i in listAccount:
        Accounts.add(i)
    root.mainloop()
