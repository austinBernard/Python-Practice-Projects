#parent class

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def user_details(self):
        print("__User details__" )
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        
#child class

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated: $", self.balance)
        
    def withdraw(self, amount):
        self.amount = amount
        if (self.amount > self.balance):
            print("Insufficent funds | Balance: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Sucessfully withdrew $", self.amount, " New balance: ", self.balance)
            
    def view_balance(self):
        self.user_details()
        print("Account balance: ", self.balance)
        
        
             
#main
person = Bank('Austin', 27, 'Male')
person.deposit(100)
person.deposit(400)
person.withdraw(100)
person.deposit(500)
person.withdraw(900)
person.user_details()
person.view_balance()