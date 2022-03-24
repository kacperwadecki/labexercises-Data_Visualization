import wikipedia

wikipedia.set_lang('pl')  # ustawienie jezyka na polski

python = wikipedia.page('Python')
mauritius = wikipedia.page('Mauritius')
galapagos = wikipedia.page('Galapagos')

# print(mauritius.url) adres url
# print(python.title) tytul
# print(python.galapagos) tresc

summary = wikipedia.summary('Python', sentences=1)
# print(summary)  # podsumowanie
