def count_words_strict(text):
    count = 0
    in_word = False

    for c in text:
        if c.isalnum() or c == '_':
            if not in_word:
                count += 1
            in_word = True
        else:
            in_word = False

    return count

print(count_words_strict("Hello, world!"))
print(count_words_strict(""))
print(count_words_strict("..."))
print(count_words_strict("a_b 1-c"))
