"""Create instances of the class."""

"""
We're creating objects that belong to that class."""

# import the class
# from >file_name>.<module_name> import <class_
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True)
#accessing/setting attributes
#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

#printing out some values
#print("my_pizza: ")
#print(my_pizza)
#print("Pizza: ")
#print(Pizza)
#print("Size Attribute: ")
#print(my_pizza.size)
#print(my_pizza.toppings)

sals_pizza: Pizza = Pizza("medium", 5, False)
#print(sals_pizza.size)

def price(input_pizza: Pizza) -> float:
    """Calculate prize of Pizza."""
    if input_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free is True:
        price += 1.00
    return price
#Calling price function
print(price(sals_pizza))
print(price(my_pizza))
#Calling price method
print(sals_pizza.price())
print(my_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings
print(my_other_pizza.toppings)
print()