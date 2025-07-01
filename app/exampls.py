import math

r = math.factorial(6)

print(r)


my_list = []

for i in range(1,6):
    my_list.append(i)

print(my_list)

print(my_list[-1])

my_list.reverse()
print(my_list)

for i in range(1, 6):
    my_list.append(i)
print(my_list)


def factorial(odd_number):
    once = 1
    for i in range(1,odd_number+1):
        once *= i 
    return once
odd_list = []
for num in my_list:
    if num % 2 == 1:
        fac = factorial(num)
        odd_list.append(fac)

print(odd_list)
        
my_list=[i*2 for i in my_list]
print (my_list)