import random

print("ceiling?")
ceiling = int(input())
number1 = random.randint(1, ceiling)
number2 = random.randint(1, ceiling)
print("how much is ",number1,"*",number2,"?")
answer = int(input())
if(answer == number1*number2):
    print("The answer is correct!")
else:
    print("The answer is not correct. The correct answer is",number1*number2)
