import random

print("How many questions?")
many = int(input())

print("ceiling?")
ceiling = int(input())

listnumber1=list()
listnumber2=list()
listanswer=list()
for x in range (many):
    number1 = random.randint(1, ceiling)
    number2 = random.randint(1, ceiling)
    listnumber1.append(number1)
    listnumber2.append(number2)
    print("how much is ",number1,"*",number2,"?")
    answer = int(input())
    listanswer.append(answer)
for i in range (many):
    q=str(listnumber1[i])+"*"+str(listnumber2[i])
    a=(listnumber1[i])*(listnumber2[i])
    print("Q"+str(i+1)+") "+q+"="+str(a))


#m = input("Want to try again (yes/no)? ")
#if (m != "yes"):
#    finish = True
