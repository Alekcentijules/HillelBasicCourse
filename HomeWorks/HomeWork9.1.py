import string

def popular_words (text, words):
    dict_words = {}
    # words_in_text = text.lower().replace([string.punctuation], "").split(" ")
    words_in_text = "".join(w if w not in string.punctuation else " " for w in text).lower().split()

    # count = 0
    # for w in words:
    #     count = words_in_text.count(w)
    #     dict_words.setdefault(words[w], 0)
    #     dict_words[w] += 1
    # for w in words:
    #     for w in words_in_text:
    #         dict_words.setdefault(w, 0)
    #         dict_words[w] += 1

    for w in words:
        dict_words[w] = words_in_text.count(w)

    return dict_words


# some_text = '''When I was One I had just begun When I was Two I was nearly new'''
# search_words = ['i', 'was', 'three', 'near']
some_text = """There were quite a few long nights, long weeks and even long weekends full of cloud 
               rendering but I couldn’t have been prouder of what my team and Lytro as a whole achieved under amazing 
               delivery pressure and a fast evolving technology stack."""
search_words = ['and', 'a', 'long', 'name']
result = popular_words(some_text, search_words)

print(result)
assert popular_words('''When I was One I had just begun When I was Two I was nearly new
                      ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')












# some_text = '''When I was One I had just begun When I was Two I was nearly new'''
# spl = some_text.split(" ")
# print(spl)