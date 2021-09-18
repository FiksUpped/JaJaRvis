from word2numberi18n import w2n
import os
import math
import operator

os.environ['w2n.lang'] = 'ru'

operations_to_replace = {
    'плюс': "+",
    'минус': "-",
    'умножить на': '*',
    'в степени': '^',
    'делить': '/',
    'процент': '%',
    'квадратный корень из': 'sqrt',
    'факториал от': 'factorial',
    'логорифм от': 'log',
    'площадь сферы': 'pi*',
}

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}



def BasicMath(command, phrase):


    parsed_phrase = ParseIncomingPhrase("два плюс три")

    print(parsed_phrase)

   #if (command == "сумма"):

   # basic_check = w2n.word_to_num("")

    #print(basic_check)




def Addition(phrase):
    print("test")


def Substraction():
    print("test")

def Multiplication():
    print("test")


def Trigonometry():
    print("test")


def Root():
    print("test")


def Factorial():
    print("test")


def Logorythm():
    print("test")

def Integral():
    print("test")

def Ssphere():
    print("test")


def ParseIncomingPhrase(phrase):

    for key in operations_to_replace.keys():

        phrase = phrase.replace(key, operations_to_replace[key])

    phrase_splitted = phrase.split(' ')

    if (len(phrase_splitted) == 3):

# Separate math calculation into two parts and operand to make them numbers instead of words

        a = w2n.word_to_num(str(phrase_splitted[0]))

        operand_ = phrase_splitted[1]

        b = w2n.word_to_num(phrase_splitted[2])

        print(ops[operand_](a,b))






       




    return phrase_splitted





BasicMath("test", "test")