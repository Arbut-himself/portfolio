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

def count_letters(input: str) -> dict:
    letter_count = {}
    for i in input:
        if i in letter_count:
            letter_count[i] += 1
        else:
            letter_count[i] = 1
    return letter_count

def count_permutations(s: str) -> int:
    letter_count = count_letters(s)
    bottom_text = 1 # it's the denominator in the combinatorics formula

    for i in letter_count:
        bottom_text = bottom_text*factorial(letter_count[i])
    permutations = int(factorial(len(s))/bottom_text)
    
    return permutations