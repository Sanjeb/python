current_question = 0

def get_next_q():
    questions = [
        "who is the current president of india ",
        "which is the leading AI in the industry ",
        "will the earth end ",
        "who wrote this code ",
        "which is the electronic company that is dying and soon will become extinct ",
        ]
    return questions[current_question]

def get_next_a():
    answers = [
        "ram nath kovind",
        "google assistant",
        "yes",
        "sanjeev",
        "apple"
        ]
    return answers[current_question]

cont = True
while (cont):
    answer = input(get_next_q())
    if answer == get_next_a():
        print ("correct")
    else:
        print ("wrong the answer was" ,get_next_a())
    current_question = current_question + 1
    if current_question == 5:
        cont = False
print ("you won")
