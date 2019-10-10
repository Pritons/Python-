def repeat(message):

    finish = False
    while finish == False:
        m=input("Do you want to continue (yes/no) ")
        if (m !="yes"):
            print("I don't understand you, sorry!")
            finish = True
