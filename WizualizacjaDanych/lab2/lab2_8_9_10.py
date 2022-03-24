from faker import Faker
import wikipedia
fake = Faker()

n: int = 10

if n == 8:
    text: str = fake.text()
    print(text)
    print(len(text))
elif n == 9:
    text: str = wikipedia.summary('Olsztyn', 1)
    print(text)
    print(text.upper())
elif n == 10:
    text: str = wikipedia.page('Guido van Rossum')
    print(text.content[-100:])
    print(len(text.content[-100:]))
