import inquirer
#this is common tools for the script

def Ilist(names,titles,possibleawns):#ask inquirer list questions and return the index of the question can ask multiple inquirer questions
#exemple with two questions:
#print(Ilist(["question1","question2"],["do you like pineapple on pizza?","choose one"],[["no","NO"],["cats","dogs"]]))
#this will return:
#
#[?] do you like pineapple on pizza?: NO
#   no
# > NO
#
#[?] choose one: cats
# > cats
#   dogs
#
#[1, 0]
#
# note if thre is a single question this return only the response as an int not a string
    questions=[]
    resp = []
    for i in range(len(names)): #generate questions based on the number of question names (there is only one per question)
        questions.append(
            inquirer.List(names[i],
                          message=titles[i],
                          choices=possibleawns[i],
                          ),
        )
    responses = inquirer.prompt(questions)#get the dict of responses to the questions
    if len(names) == 1: # if there is only one question
        return possibleawns[0].index(responses[names[0]]) # check the awnser index in the possible anwser for the response for the sole quesion wich his name is stored in names
    else: #if there is more than one questions
        for i in range(len(responses)): #for each responses loop
            resp.append(possibleawns[i].index(responses[names[i]])) #add to the rsp list the index in possible awnsers of the selected awnser for the question i
        return resp #return the list of responses
