def second_index(text, some_str):
    first_substr = text.find(some_str)
    second_text = text.find(some_str, first_substr + 1)
    count_second_text = text.count(some_str)

    # count_second_text = text.count(some_str) if text.count(some_str) >= 2 else return None

    if not text or not some_str:
        return 'The conversation requires at least two byte of text!'

    return second_text if count_second_text >= 2 else None

user_input_str = input("Enter a text: ")
user_input_substr = input("Enter a text fragment to be found: ")
result = second_index(user_input_str, user_input_substr)

print(result)
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')















