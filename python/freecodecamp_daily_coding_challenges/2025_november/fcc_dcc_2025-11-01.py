def verify(message: str, key: str, signature: int) -> bool:

    count = 0
    
    alpha_only_message = ''.join(filter(str.isalpha, message))
    alpha_only_key = ''.join(filter(str.isalpha, key))

    for character in alpha_only_message:
        if character.isupper():
            count += (ord(character)-38)
        else:
            count += (ord(character)-96)

    for character in alpha_only_key:
        if character.isupper():
            count += (ord(character)-38)
        else:
            count += (ord(character)-96)

    return count == signature

print(verify("foo", "bar", 57))