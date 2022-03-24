def palindrom(word: str) -> bool:
    tmp: str = word[::-1]
    if tmp == word:
        return True
    else:
        return False


print(palindrom("kajak"))