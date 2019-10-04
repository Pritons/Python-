

def repeat(message, number):
    print()
    for i in range(number):
        print(str(i+1)+": ",message)
    print()
finish = False
while finish == False:
    print()
    print("give a message, please:")
    message = input()
    print("give a number, please")
    try:
        number = int(input())
        repeat(message, number)
    except ValueError:
        print("not an integer!")
