from typing import Dict

di: Dict[str, str]= {
    'jeden': 'one',
    'dwa': 'two',
    'trzy': 'three'
}

while True:
    word: str = str(input('Wprowadz slowo do przetlumaczenia: '))
    if word == 'end':
        break
    else:
        tmp1: bool = False
        for i in di:
            if i == word:
                print(di[i])
                tmp1 = True

        if not tmp1:
            di[input("Wprowadz polskie tlumaczenie: ")] = input("Wprowadz angielskie tlumaczenie: ")