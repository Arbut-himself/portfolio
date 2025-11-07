def factorial(input: int) -> int:

    '''
    Just to be clear, this function is reinventing the wheel.
    In reality you can just import math and use math.factorial().
    But for these code challenges I want to have as few imports
    as I can possibly manage, building everything to the lowest
    level that my skillset at the time allows. And as it happens
    making a factorial function isn't that hard all things considered.
    '''
    
    fact = 1
    for i in range(1, input+1):
        fact = fact * i
    return fact

def combinations(cards: int) -> int:
    combos = int(factorial(52)/((factorial(cards))*(factorial(52-cards))))
    return combos