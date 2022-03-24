def calc(x: int, y: int, char: str) -> int:
    if char == '+':
        return x + y
    elif char == '-':
        return x - y


x: int = int(input('Wprowadz x : '))
y: int = int(input('Wprowadz y : '))
char: str = str(input('Wprowadz znak : '))
print(calc(x, y, char))