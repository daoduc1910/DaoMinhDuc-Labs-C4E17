from random import *
import evaluate

def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)

    op = choice(["+", "-", "*", "/"])

    result = evaluate.calc(m, n, op)
    error = choice([-1, 0, 0, 1])
    dis_result= result + error
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    if display_result == result:
        if user_choice == True:
            return True
        else:
            return False
    else:
        if user_choice == True:
            return False
        else:
            return True
