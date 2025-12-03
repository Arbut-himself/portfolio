def to_snake(camel: str) -> str:
    snake = ""
    for i in camel:
        if i.islower():
            snake = ''.join([snake, i])
        else:
            snake = '_'.join([snake, i.lower()])
    return snake