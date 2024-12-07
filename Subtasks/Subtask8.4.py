def reverse_words(sentence):
    return " ".join(sentence[::-1].split(" ")[::-1])

result = reverse_words("Hello Brazer")
print(result)