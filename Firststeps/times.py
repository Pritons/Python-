import random

print("How many questions?")
many = int(input())

print("ceiling?")
ceiling = int(input())


for x in range (many):
    number1 = random.randint(1, ceiling)
    number2 = random.randint(1, ceiling)
    print("how much is ",number1,"*",number2,"?")
    answer = int(input())
