def kbc():
    print("welcomr to KBC game")
    questions=["how many contients are there?","what is the capital of india?","navgurukul main kaun se course padhaya jata hai?"]
    options=[["four","nine","seven","eight"],["chandigad","bhopal","chennai","delhi"],["agriculture","scince","engineering","tourisim"]]
    answer=["seven","delhi","engineering"]
    i=0
    while i<len(questions):
        print("your qusetions in your screen")
        print(questions[i])
        print(options[i])
        choice=input("choice one option")
        if choice==answer[i]:
            print("correct")
        else:
            print("wrong")
            break
        i=i+1
kbc()
