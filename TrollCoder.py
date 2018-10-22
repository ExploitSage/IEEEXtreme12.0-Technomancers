# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy
import sys

def send(prefix, guess):
    query = prefix + " ".join(guess)
    print(query)
    sys.stdout.flush()
    
def answer(guess):
    send("A ", guess)
    
def query(guess):
    send("Q ", guess)
    return int(input())

length = get_number()
guess = ["0"] * length

numCorrect = query(guess)

for i in range(0, length):
    if numCorrect == length:
        answer(guess)
    else:
        guess[i] = "1"
        if i == (length - 1):
            answer(guess)
        else:
            newNumCorrect = query(guess)
            if newNumCorrect > numCorrect:
                numCorrect = newNumCorrect
                continue
            else:
                guess[i] = "0"


