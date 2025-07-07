from logging_decorators import decorator

def greet(name):
    print(f"helloo {name} in python")

# greet("ali")
@decorator
def add(a: float, b: int):
    return a + b

# result = add(45, 45)
# print(result)

def power(num, exp=2):
    return num ** exp
# print(power(4, 3))

def rgb(g, b, r=45):
    return f"rgb({r}, {g}, {b})"


# print(rgb(b=147,g=100))

def total(*nums):
    print(type(nums))
    return sum(nums)
# my_tuple = (1, 2, 5, 8)
# print(total(1, 2, 5, 8))
