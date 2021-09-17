from word2numberi18n import w2n
import math


operations_to_replace = {
    'плюс': "+",
    'умножить на': '*',
    'квадратный корень из': 'sqrt',
    'факториал от': 'factorial',
    'логорифм': 'log',
    'площадь сферы': 'pi*',
}



def BasicMath(command, phrase):


    parsed_phrase = ParseIncomingPhrase("два умножить на три")

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



       




    return phrase_splitted





BasicMath("test", "test")