import easygui,sys

pts = 0

def askQuestions():
    pts = 0
    q1 = easygui.integerbox("On a scale of 1 to 10, what is your stress level", argLowerBound=1, argUpperBound=10)
    pts += int(q1)*100
    q2 = easygui.integerbox("How many hours per week do you spend studying?", argLowerBound=0, argUpperBound=75)
    pts += int(q2)*100
    q2 = easygui.integerbox("How many hours do you spend playing games or doing recreational activities?", argLowerBound=0, argUpperBound=75)
    pts -= (int(q2)-1)*100
    q3 = easygui.buttonbox("How many friends do you have?", choices=["Friends? What friends?", "Not many", "A few", "Quite a lot", "It's over 9000"])
    if q3=="Friends? What friends?":
        pts+=750
    elif q3=="It's over 9000":
        pts-=75
    elif q3=="A few":
        pass
    elif q3=="Not many":
        pts+=250
    elif q3=="Quite a lot":
        pts-=250
    q4 = easygui.choicebox("Do you excercise regularly? If so, do you like it?", choices=["I hate excercising, but I have to", "I like excercising, so I do it a lot", "Meh", "I don't like excercising, so I don't do it much", "I don't particularly like it, but it is good for my health"])
    if q4=="I hate excercising, but I have to":
        pts+=500
    elif q4=="I like excercising, so I do it a lot":
        pts-=500
    elif q4=="Meh":
        pass
    elif q4=="I don't like excercising, so I don't do it much":
        pts+=250
    elif q4=="I don't particularly like it, but it is good for my health":
        pts-=250
    q5 = easygui.choicebox("When do you do your homework", choices=["We had homework today?", "I rush through it in the morning when I finally remember", "At school", "Right after school", "After a break or other activities"])
    if q5=="We had homework today?":
        pts+=1000
    elif q5=="I rush through it in the morning when I finally remember":
        pts+=500
    elif q5=="Right after school":
        pts-=500
    elif q5=="At school":
        pts-=1000
    elif q5=="After a break or other activities":
        pass
    return pts

start = easygui.buttonbox("Welcome to the Stressmeter", choices=["Begin", "Exit"])
if str(start) == "Begin":
    pts = askQuestions()
    if pts < 0:
        pts=0
    if pts<=2000:
        easygui.msgbox("Your score was "+str(pts)+". You are not stressed. What are you doing here?")
    elif pts <= 4000:
        easygui.msgbox("Your score was "+str(pts)+". You are slightly stressed. Nothing you can't deal with.")
    elif pts <= 6000:
        easygui.msgbox("Your score was "+str(pts)+". You are stressed. Possibly a break would be in order.")
    elif pts <= 8000:
        easygui.msgbox("Your score was "+str(pts)+". You are extremely stressed. Take it easy. Go take a few days off")
    elif pts <= 10000:
        easygui.msgbox("Your score was "+str(pts)+". You are extremely extremely stressed. Go see a psychiatrist.")
    else:
        easygui.msgbox("Your score was "+str(pts)+". OMG you are so stressed!!!! Please see a psychologist to preserve your mental health")
    feedback = easygui.enterbox("Please give some feedback")
    feedbackfile = open('feedback.txt', 'a')
    feedbackfile.write(feedback)
    feedbackfile.close()
    print "Thank you for your feedback"
elif str(start) == "Exit":
    print "Exit Successful"
    sys.exit()
