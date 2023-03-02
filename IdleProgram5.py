import random 
import math


def addition():
    user_ans = int(input())
    add = number_one + number_two
    if user_ans == add:
        number_correct = number_correct + 1
        print('That is correct!')
        return
    else:
        print('That is incorrect')
        return
    


def subtraction():
    user_ans = int(input())
    subtract = number_one - number_two
    if user_ans == subtract:
        print('That is correct!')
        return 
    else:
        print('That is incorrect')
        return
    

def multiplication():
    user_ans = int(input())
    multiply = number_one * number_two
    if user_ans == multiply:
        print('That is correct!')
        return
    else:
        print('That is incorrect')
        return


def division():
    user_ans = int(input())
    divide = number_one // number_two
    if user_ans == divide:
        print('That is correct!')
        return
    else:
        print('That is incorrect')
        return

def points():
    score = total_points / 10
    print(f'You got a {score} percent!')

number_correct = 0

for i in range(0,10):
    number_one = random.randint(0,100)
    number_two = random.randint(0,100)
    operators = ['+', '-', '//', '*']
    operator = random.choice(operators)
    print(f'What is: {number_one} {operator} {number_two} =')
    if operator == '+':
        addition()
    elif operator == '-':
        subtraction()
    elif operator == '//':
        division()
    elif operator == '*':
        multiplication()

total_points = number_correct

points()