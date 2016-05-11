# Data Hiding
class MyClass():

    def __init__(self):
        self._private1 = 'Weakly private property'
        self.__private2 = 'Strongly private property'

    def _private3(self):
        return 'Weakly private method'

    def __private4(self):
        return 'Strongly private method'

c = MyClass()
print(c._private1)
# print(c.__private2) # AttributeError
print(c._MyClass__private2)
print(c._private3())
# print(c._private4()) # AttributeError
print(c._MyClass__private4())


# Class Methods
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())
print(square.calculate_perimeter())


# Static Methods and Property
class Pizza:

    def __init__(self, name, toppings):
        self.name = name
        self.toppings = toppings
        self._nutella_allowed = False

    def __repr__(self):
        return 'Pizza %-40s\n%40s' % (self.name, ', '.join(self.toppings))

    @classmethod
    def new_margherita(cls):
        return cls('Margherita', ['tomato', 'cheese', 'origano'])

    @property
    def pineapple_allowed(self):
        return False

    @property
    def nutella_allowed(self):
        return self._nutella_allowed

    @nutella_allowed.setter
    def nutella_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._nutella_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

name = 'Captain America'
ingredients = ['tomato', 'cheese', 'onions', 'spam']
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(name, ingredients)
print(pizza)
pizza = Pizza.new_margherita()
print(pizza)
print('Pineapple allowed: %r' % pizza.pineapple_allowed)
print('Nutella   allowed: %r' % pizza.nutella_allowed)
print('Allowing Nutella...')
pizza.nutella_allowed = True
print('Nutella   allowed: %r' % pizza.nutella_allowed)
