nums = [i for i in range(1, 11, 1)]

# print(nums)

# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# even = lambda x: x % 2 == 0
# result =[x for x in nums if (even(x=x))(x)]


import string , random

def password(length, digits=True, sympols=False):
    total_list = []

    string_list = list(string.ascii_letters)
    digit_list = list(string.digits)
    symp = list(string.punctuation)

    total_list = string_list + digit_list if digit_list else None
    total_list += symp if symp else None

    password_choices = random.choices(total_list, k=length)
    my_password = "".join(password_choices)

    return my_password

print(password(20))