def mirror(initial_string: str) -> str:
    new_string = initial_string
    for i in range(1, len(initial_string)+1):
        new_string += initial_string[-i]
    return new_string