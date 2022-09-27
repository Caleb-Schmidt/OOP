from datetime import datetime as dt
class User():

    def __init__(self, first_name, last_name, email, created_on):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_on = dt.utcnow()

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        """Human Readable output -- should be unique"""
        return f"<Person | {self.full_name}>"

    def __repr__(self):
        return f"<Employee | {self.last_name} {self.created_on.strftime('%c')}>"

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        self.email = other.email

    def change_first_name(self, new_name):
        self.first_name = new_name
    
    def change_last_name(self, new_name):
        self.last_name = new_name


class Employee(User):
    def __init__(self, first_name, last_name, email, created_on, home_address, security_level, department):
        super().__init__(first_name, last_name, email, created_on)
        self.home_address = home_address
        self.security_level = security_level
        self.department = department

    def change_department(self, new_department):
        self.department = new_department

class Customer(User):
    def __init__(self, first_name, last_name, email, created_on, shipping_address, billing_address, purchase_history):
        super().__init__(first_name, last_name, email, created_on)
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_history = purchase_history


    def change_shipping_address(self, new_address):
        self.shipping_adress = new_address

    def change_billing_address(self, new_address):
        self.billing_adress = new_address


marco = Employee("Marco", "Cladimere", "marco@gmail.com", dt.utcnow(), "123 silver st.", 10, "sales")
john = Employee("John", "Gutentag", "john@gmail.com", dt.utcnow(), "123 silver st.", 10, "sales")
marcus = Employee("Marcus", "Shteven", "marcus@gmail.com", dt.utcnow(), "123 silver st.", 10, "sales")

brad = Customer("Brad", "Shteven", "brad@gmail.com", dt.utcnow(), "123 silver st.", "123 silver st.", "bought shoes")
jonathon = Customer("Jonathon", "Stewart", "jonathon@gmail.com", dt.utcnow(), "123 silver st.", "123 silver st.", "bought shoes")
connor = Customer("Connor", "Davidson", "connor@gmail.com", dt.utcnow(), "123 silver st.", "123 silver st.", "bought shoes")

people = [marco, john, marcus, brad, jonathon, connor]
people.reverse()
print(people)
