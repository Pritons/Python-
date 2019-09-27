#Note:

# A function that prints the message number of times:
def repeat(message, number):
    print() #an empty line first. Looks better.
    for i in range(number):
        # Adds a growing number before the message:
        print(str(i+1)+": ",message)
    print() # An empty line

finish = False
while finish == False:
    print() # Adds a line break.
    print("give a message, please:")
    # Retrieves the message given by the user:
    message = input()
    print("Give a number, please")
    # Important: if ValueError, goes to except block.
    try:
        number = int(input()) # Error if input not good
        repeat(message, number) # Function call
    except ValueError:
        print("Not an integer!")

        # To continue? Note the alternative syntax:
    m = input("Want to try again (yes/no)? ")
    if (m != "yes"):
        finish = True
