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
    return pts

start = easygui.buttonbox("Welcome to the Stressmeter", choices=["Begin", "Exit"])
if str(start) == "Begin":
    pts = askQuestions()
    if pts < 0:
        pts=0
    if pts<=1000:
        easygui.msgbox("Your score was "+str(pts)+". You are not stressed. What are you doing here?")
    elif pts <= 2500:
        easygui.msgbox("Your score was "+str(pts)+". You are slightly stressed. Nothing you can't deal with.")
    elif pts <= 5000:
        easygui.msgbox("Your score was "+str(pts)+". You are stressed. Possibly a break would be in order.")
    elif pts <= 7500:
        easygui.msgbox("Your score was "+str(pts)+". You are extremely stressed. Take it easy. Go take a few days off")
    elif pts <= 10000:
        easygui.msgbox("Your score was "+str(pts)+". You are extremely extremely stressed. Go see a psychiatrist.")
    else:
        easygui.msgbox("Your score was "+str(pts))
    feedback = easygui.enterbox("Please give some feedback")
    print feedback
    print "Thank you for your feedback"
elif str(start) == "Exit":
    print "Exit Successful"
    sys.exit()
