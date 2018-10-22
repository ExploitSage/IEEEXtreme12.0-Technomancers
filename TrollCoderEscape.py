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
# import numpy
# import scipy
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

num_cases = get_number()
for _ in range(0, num_cases):
    length = get_number()
    guess = ["0"] * length
    
    numCorrect = query(guess)
    answered = False
    
    for i in range(0, length, 3):
        if numCorrect == length:
            answer(guess)
            answered = True
            break
        else:
            if i == 99:
                break
            guess[i] = "1"
            guess[i + 1] = "1"
            guess[i + 2] = "1"
            
            newNumCorrect = query(guess)
            if newNumCorrect == length:
                answer(guess)
                answered = True
                break
            if newNumCorrect == (numCorrect + 3): # all are, in fact, ones
                numCorrect = newNumCorrect
                continue
            elif newNumCorrect == (numCorrect - 3): # all are, in fact, zeroes
                guess[i] = "0"
                guess[i + 1] = "0"
                guess[i + 2] = "0"
                numCorrect = newNumCorrect + 3
                continue
            elif newNumCorrect == numCorrect - 1: # one's a one, two are zeroes
                numCorrect = newNumCorrect
                guess[i] = "1"
                guess[i + 1] = "0"
                guess[i + 2] = "0"
                newNumCorrect = query(guess)
                if newNumCorrect == numCorrect + 2: # it was 100
                    numCorrect = newNumCorrect
                    continue
                # wasn't 100
                numCorrect = newNumCorrect
                guess[i] = "0"
                guess[i + 1] = "1"
                guess[i + 2] = "0"
                newNumCorrect = query(guess)
                if newNumCorrect == numCorrect + 2:
                    numCorrect = newNumCorrect
                    continue
                guess[i] = "0"
                guess[i + 1] = "0"
                guess[i + 2] = "1"
                numCorrect = newNumCorrect + 2
                continue
            # ------------------------------
            elif newNumCorrect == numCorrect + 1: # two are ones, one's a zeroes
                numCorrect = newNumCorrect
                guess[i] = "1"
                guess[i + 1] = "1"
                guess[i + 2] = "0"
                newNumCorrect = query(guess)
                if newNumCorrect == numCorrect + 1: # yay we got it 110
                    numCorrect = newNumCorrect
                    continue
                # must be either 101 or 011
                numCorrect = newNumCorrect
                guess[i] = "1"
                guess[i + 1] = "0"
                guess[i + 2] = "1"
                newNumCorrect = query(guess)
                if newNumCorrect == numCorrect + 2: # got it 101
                    numCorrect = newNumCorrect
                    continue
                # must be 011
                guess[i] = "0"
                guess[i + 1] = "1"
                guess[i + 2] = "1"
                numCorrect = newNumCorrect + 2
                continue
            else: # oh no my algorithm is wrong
                raise(ValueError)
    if answered == False:
        if length == 6:
            answer(guess)
        else:
            guess[99] = "1"
            numCorrect = query(guess)
            if numCorrect == length:
                answer(guess)
            else:
                guess[99] = "0"
                answer(guess)