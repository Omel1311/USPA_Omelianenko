class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"{self.name} {self.age} {self.address}"


customer1 = Customer("John", 30, "123 Main St")
print(customer1)

class Order:
    def __init__(self, customer, items, total):
        self.customer = customer
        self.items = items
        self.total = total

    def __str__(self):
        return f"{self.customer} {self.items} {self.total}"


order1 = Order(customer1, "apple", 10)
print(order1)