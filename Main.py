question = {1:"Who is the bass player?",2:"Who is the drummer?",3:"Who is the Guitar player?",4:"How many bass players have they had?",5:"What city did they come from?",6:"In what year did they win Rockquest?",7:"How many full legth studio albums do they have?",8:"What record label are they signed with?"}
answerlist = {1:"1."}
answers = {1:"turanga morgan edmonds",2:"henry de jong"}
score = 0

for value in question:
    print(question[value])
    print(answerlist[value])
    answering = input()
    answering = answering.lower()
    if answering == answers[value]:
        print('Answer correct')
        score = score + 1 
    elif answering != answers[value]:
        print('you got it wrong')

percentscore = score * (100 / len(question))

print(f'You got {percentscore}')