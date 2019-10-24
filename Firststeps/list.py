import random
def randintlist(len, ceiling):
    list1 = list()

    for x in range (len):
        number = random.randint(1, ceiling)
        list1.append(number)
    return list1

print(randintlist(5, 10))
