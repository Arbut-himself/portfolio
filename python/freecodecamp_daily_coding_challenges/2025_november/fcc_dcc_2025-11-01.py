def alphabetize(input: str) -> str:
    output = ''.join(filter(str.isalpha, input))
    return output

def count_letter_values(input: str) -> int:
    count = 0
    for character in input:
        if character.isupper():
            count += (ord(character)-38)
        else:
            count += (ord(character)-96)
    return count
        
def verify(message: str, key: str, signature: int) -> bool:
    count = 0

    alpha_only_message = alphabetize(message)
    alpha_only_key = alphabetize(key)

    count += count_letter_values(alpha_only_message)

    count += count_letter_values(alpha_only_key)

    return count == signature