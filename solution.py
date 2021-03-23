import random


R1=int(input("1st Range Side:\t"))
R2=int(input("2nd Range Side:\t"))

R = random.randint(R1, R2)
print("Random Numbwer is:\t",R)
count=0

while (True):
    GN = int(input("Number guessing:\t"))
    if (GN >=R1 and GN <= R2):
        count += 1
        if R == GN:
            print("you did it!")
            print("you takes",count,"rounds to guessed")
            break
        elif R > GN:
            print("You guessed under the random!")
        elif R < GN:
            print("You guessed above the random!")
    else:
        print("Error :Out of Range![",R1,",",R2,"]")    
    

