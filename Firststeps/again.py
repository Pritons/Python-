def repeat():

    finish = False
    while finish == False:
        m=input("Do you want to continue (yes/no) ")
        if (m =="yes"):
            print("Try agin.")

        elif (m =="no"):
            finish = True
        else:
            print("I don't understand you, sorry!")
repeat()
