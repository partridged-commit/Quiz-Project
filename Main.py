question = {1:"How many bass players have there been?",2:"Who is the bass player?",3:"What city did they come from?",4:"In what year did they win Rockquest?",5:"How many full legth studio albums do they have?",6:"What record label are they signed with?"}
answerlist = {1:"1. 1   2. 2   3. 3",2:"1. Turanga Morgan Edmonds   2. Wyatt Channings   3. Ethan Trembath",3:"1. Wellington   2. Auckland   3. Tauranga",4:"1. 2014   2. 2015   3.2016",5:"1. 1   2. 2   3. 3",6:"1. Eclipse Records   2. Napalm Records   3. Road Runner Records"}
answers = {1:"3",2:"1",3:"2",4:"3",5:"2",6:"2"}
score = 0


for value in question:
    print(question[value])
    print(answerlist[value])
    print(answers[value])

    answering = input()


    if answering.isnumeric() == False:                      # This section checks for non numerical inputs, lets the user enter a correct input,
        while answering.isnumeric() == False:               # and then set the variable type to integer
            print("Please enter a number input")
            answering = input()
    answering = int(answering)


    if answering <= 3 and answering > 0:
        if answering == answers[value]:
            print('Answer correct')
            score = score + 1 
        elif answering != answers[value]:
            print('you got it wrong')
    else:
        print("Please enter a valid answer")
        while answering > 3 or answering < 0:
            if answering == answers[value]:
                print('Answer correct')
                break
                score = score + 1 
            elif answering != answers[value] and answering > 3 or answering < 0:
                print('you got it wrong')
                break
            elif answering > 3 or answering < 0:
                print("That is still not a valid answer")


percentscore = score * (100 / len(question))

print(f'You got {percentscore}')