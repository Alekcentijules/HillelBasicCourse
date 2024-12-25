import codecs
import os
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    # print(html)

    text = ""
    tag = False

    for char in html:
        if char == "<":
            tag = True
        elif char == ">":
            tag = False
        elif not tag:
            text += char
    # print(text)

    # lines = []
    # for line in text.split('\n'):
    #     if line.strip():
    #         # line.strip()
    #         lines.append(line.strip())
    # print(lines)
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    with open(result_file, "w", encoding="utf-8") as file:
        file.write('\n'.join((lines)))
    # print(lines)

    return lines

delete_html_tags("C:/Users/ohala/Downloads/draft.html")










