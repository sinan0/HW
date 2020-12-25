name=input("What is your name?")
print("WELCOME",name)
import random
print("Rulles:\n1.You have the right to answer 8 wrong answers.\n2.If you enter the same letter again, your right will decrease.\n3.Enter lower case.")
animal=["dog","cat","rabbit","parrot","dolphin","sheep","bird","crab","ducks","goat","eagle","lion","owl","zebra","crocodie","mouse","hamster"]
word=list(random.choice(animal))
j=len(word)
i=8
line=list(len(word)*"_")
while i>0:
    answer=input("Please enter letter:")
    if not answer in word or answer in line :
        i-=1
        if (i==0):
            print("GAME OVER")
            break
        print(i,"you have rights left")
        continue

    cnt=word.count(answer)
    while cnt>0:
        indx=word.index(answer)
        line[indx]=answer
        word[indx]='0'
        cnt-=1
        j-=1
    print(line)
    if(j==0):
        print("YOU WON")
        break
