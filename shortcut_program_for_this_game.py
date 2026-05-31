import random
# 1 for snake s more powerful then water
# -1 for water is more powerful then gun
# 0 for gun is more powerful then snake
computer = random.choice([-1,0,1])
youstr =input("enter game code: ")
youdict ={"s":1,"w":-1,"g":0}
you=youdict[youstr]
reversedict ={1:"snake",-1:"water",0:"gun"}
print(f"you choose {reversedict[you]} and computer choose {reversedict[computer]}")
if(computer==you):
    print("It's a Draw")
else:
    if((computer-you)==-1 or (computer-you)==2):
        print("you lose")
    else:
        print("you win")
    # if(computer==-1 and you==1):  -2 # ye maine kuch es parkar likha jaise agar mai (-1)-1=-2
    #     print("you win")
    # elif(computer==-1 and you==0):  -1#similarly -1-0=-1
    #     print("you loose")
    # elif(computer==1 and you==-1):  2
    #     print("you loose")
    # elif(computer==1 and you==0):   1
    #     print("you win")
    # elif(computer==0 and you==-1):  1
    #     print("you win")
    # elif(computer==0 and you==1):   -1
    #     print("you loose")
    # else:
    #     print("something went wrong")
    

