"""This Program is a quiz on the New Zealand band, Alien Weaponry."""


question = {1:"1. How many bass players have there been?",2:"2. Who is the bass player?",3:"3. What city did they come from?",
            4:"4. In what year did they win Rockquest?",5:"5. How many full legth studio albums do they have?",6:"6. What record label are they signed with?"}

answerlist = {1:"1. One   2. Two   3. Three",2:"1. Turanga Morgan Edmonds   2. Wyatt Channings   3. Ethan Trembath",
              3:"1. Wellington   2. Auckland   3. Tauranga",4:"1. 2014   2. 2015   3.2016",
              5:"1. One   2. Two   3. Three",6:"1. Eclipse Records   2. Napalm Records   3. Road Runner Records"}

answers = {1:3,2:1,3:2,4:3,5:3,6:2}
score = 0

print()
print("This is a quiz on the New Zealand band, Alien Weaponry.")
print("Answer the questions by inputting the number beside your chosen answer")
print()

for value in question:
    print(question[value])                                     # This section gets the question and the list of questions from their respective 
    print(answerlist[value])                                   # dictionaries, and prints them

    user_input = input()


    if user_input.isnumeric() == False:                        # This section checks for non numerical inputs, lets the user enter a correct input,
        while user_input.isnumeric() == False:                 # and then set the variable type to integer
            print("Please enter a number input")
            user_input = input()
    user_input = int(user_input)


    if  user_input < 4 and user_input > 0:                     # This is the section that runs for regular expected inputs
        if user_input == answers[value]:
            print('Answer correct')
            score = score + 1 
        else:
            print('you got it wrong')


    else:                                                      # This part of the code handles inputs that are not assigned to answers and then non numerical inputs after that,
        while user_input > 4 or user_input <= 0:               # it tells the user this and lets them input a valid answer.
            print("Please enter a valid number")
            user_input = input()
            while user_input.isnumeric() == False:                 
                print("Please enter a number input")
                user_input = input()
            user_input = int(user_input)

        if user_input == answers[value]:                       # This part is a copy of the expected input section, checking f the user's answer is correct
            print('Answer correct')                            # after making sure it's valid.
            score = score + 1 
        else:
            print('you got it wrong')



percentscore = score * (100 / len(question))                   # This final part calculates and tells the user their score, and sends the user a message accordingly 
print(f'You got {percentscore}')
if percentscore < 50:
    print("you're trash")
elif percentscore < 80:
    print("Good Job")
elif percentscore == 100:
    print("Perfect Score")
