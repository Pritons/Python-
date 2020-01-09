import random
def randintlist(len, ceiling):
    list1 = list()

    for x in range (len):
        number = random.randint(1, ceiling)
        list1.append(number)
    list1.sort()
    return list1
print(randintlist(10, 20))
