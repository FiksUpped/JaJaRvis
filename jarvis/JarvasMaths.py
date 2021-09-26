from word2numberi18n import w2n
import os
import math
import operator

os.environ['w2n.lang'] = 'ru'

operations_to_replace = {

#Two arguments formula

    'плюс': "+",
    'минус': "-",
    'умножить на': '*',
    'в степени': '**',
    'делить на': '/',
    'логорифм от': 'log',

#One argument formula

    'квадратный корень из': 'sqrt',
    'факториал от': 'factorial',
    'двоичный от': 'log2',
    'десятичный от': 'log10',

#Geometry

    'площадь сферы': 'pi*',
}

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,  # use operator.div for Python 2
    '**' : operator.pow,
    'log' : math.log,
    'log2' : math.log2,
    'log10' : math.log10,
    'sqrt': math.sqrt,
    'factorial': math.factorial,
}



def MathRequestParser(command, phrase):


    parsed_phrase = ParseIncomingPhrase("8 логорифм от 2")

    print(parsed_phrase)

   #if (command == "сумма"):

   # basic_check = w2n.word_to_num("")

    #print(basic_check)


def MathCalculations(parsed_math_phrase):


    if (len(parsed_math_phrase) == 3):

        # Separate math calculation into two parts and operand to make them numbers instead of words

        a = w2n.word_to_num(str(parsed_math_phrase[0]))

        operand_ = parsed_math_phrase[1]

        b = w2n.word_to_num(parsed_math_phrase[2])

        return (ops[operand_](a, b))



    elif (len(parsed_math_phrase) == 2):

        number_to_count = int(parsed_math_phrase[1])

        return (ops[parsed_math_phrase[0]](number_to_count))






def HardMathCalculations():

    print("test")

def Trigonometry():
    print("test")

def Integral():
    print("test")

def Ssphere():
    print("test")


def ParseIncomingPhrase(phrase):

    for key in operations_to_replace.keys():

        phrase = phrase.replace(key, operations_to_replace[key])

    phrase_splitted = phrase.split(' ')

    print(phrase_splitted)


    return  MathCalculations(phrase_splitted)





MathRequestParser("test", "test")