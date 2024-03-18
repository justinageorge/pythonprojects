print("welocme to this computer quiz")
playing=input("do you want to play\t")
if playing.lower() != "yes":
    quit()
print("okay,lets play")    
score=0
answer = input("what is ur cpu stands for\t")
if answer.lower() == "central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("what is the colour of orange\t")
if answer.lower() == "orange":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("what is yor pets name\t")
if answer.lower() == "kevin":
    print("correct")
    score+=1
else:
    print("incorrect")

print(f"you got {score} marks in quiz")    
print (f"you got {(score/3*100)} percentage in this quiz")
        