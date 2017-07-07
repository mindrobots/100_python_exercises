# English to Portuguese translator, using this dictioanary
d = dict(weather = "clima", earth = "terra", rain = "chuva")
# add error handling to 66.py (already did that)
# points 3

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
    print("We couldn't find that word!")
# more pythonic
'''
def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "That word does not exist."

word = input("Enter word: ")
print(vocabulary(word))
'''
