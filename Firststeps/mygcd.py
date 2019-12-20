def mygcd(a,b):
    if(b==0):
        return a
    else:
        return mygcd(b,a%b)

a = 60
b= 48

print ("The gcd of 60 and 48 is : "+str(mygcd(60,48)))
print ("The gcd of 1 and 1 is : "+str(mygcd(1,1)))
print ("The gcd of 4 and 2 is : "+str(mygcd(4,2)))
print ("The gcd of 8 and 4 is : "+str(mygcd(8,4)))
print ("The gcd of 10 and 15 is : "+str(mygcd(10,15)))
