# English to Portuguese translator, using this dictioanary
d = dict(weather = "clima", earth = "terra", rain = "chuva")
# points 2

def lookup_word(word):
    if word in d:
        translation = d[word]
    else:
        translation = None
    return translation

word = input('Enter word: ')
translated = lookup_word(word)
if translated:
    print(translated)
else:
    print('{0} is not in the dictionary!'.format(word))
