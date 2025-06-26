# degree = int(input("enter the degree: "))
# degree = None
# if degree > 99:
#     # print("A")
#     pass

# if degree < 100 and degree >= 90:
#     # print("B")
#     pass

# if degree <= 90 and degree >= 80:
#     # print("C")
#     pass

numbers = [11, 12, 13, 14, 15, 16]

odds = []
for n in numbers:
    if n < 0:
        break
    if n % 2 == 0:
        continue
    odds.append(n)

print(odds)


fruits = ["apple", "banana", "ananas"]

for fruit in fruits:
    print(f"{fruit.title()} -> length {len(fruit)}")


