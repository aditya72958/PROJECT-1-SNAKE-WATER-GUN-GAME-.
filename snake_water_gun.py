import random
# 1 for snake is more powerful then water
# -1 for water is more powerful then gun
# 0 for gun is more powerful then snake
youdict ={"s":1,"w":-1,"g":0}
reversedict ={1:"🐍snake",-1:"💧water",0:"🔫gun"}
you_score=0
com_score=0
print("s = snake 🐍")
print("w = water 💧")
print("g = gun 🔫")
print("GAME START 🎮: ")
for i in range(1,6):#this loop use because i make 5 round match.
    print(f"🎯round{i}: ")
    computer = random.choice([-1,0,1])
    youstr =input("enter game code: ").lower()
    if youstr in youdict:
        you=youdict[youstr]
        print(f"you choose {reversedict[you]} and computer💻 choose {reversedict[computer]}")
        if(computer==you):
            print("🤝 It's a Draw 🤝")
            you_score=you_score+1
            com_score=com_score+1
        else:
            if(computer==-1 and you==1):
                print("🎉 you win! 🏆")
                you_score=you_score+2
                com_score=com_score+0
            elif(computer==-1 and you==0):
                print("❌ you loose 😢")
                you_score=you_score+0
                com_score=com_score+2
            elif(computer==1 and you==-1):
                print("❌ you loose 😢")
                you_score=you_score+0
                com_score=com_score+2
            elif(computer==1 and you==0):
                print("🎉 you win! 🏆")
                you_score=you_score+2
                com_score=com_score+0
            elif(computer==0 and you==-1):
                print("🎉 you win! 🏆")
                you_score=you_score+2
                com_score=com_score+0
            elif(computer==0 and you==1):
                print("❌ you loose 😢")
                you_score=you_score+0
                com_score=com_score+2
            else:
                print("something went wrong")
                
    else:
        print("YOU CHOOSE WRONG ❌❌❌")
        print("Pease input s for snake, w for water and g for gun")
        print("Please restart the game")
        break
        #sometime we choose input different word such like gun aditya or anything then it restart the game and show you choose wrong.
print("your score is 📊: ",you_score)
print("computer score is 📊: ",com_score)
if(you_score>com_score):
    print("You are the winner of this complete round 🎉🎉🎉")
elif(com_score>you_score):
    print("Computer💻 is the winner of this complete round 🎉🎉🎉")
else:
    print("draw the complete round.")
print("YOU PLAY NICE...🔄 Try Again!...🐍💧🔫")

