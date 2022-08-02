import ex22
sentence = "The quick brown fox jumps over the lazy dog"
words = ex22.break_words(sentence)
print(words)

sorted_words = ex22.sort_words(words)
print(sorted_words)


ex22.print_first_word(words)
ex22.print_last_word(words)


print(words)

ex22.print_first_word(sorted_words)
ex22.print_last_word(sorted_words)
print(sorted_words)

sorted_words = ex22.sort_sentence(sentence)
print(sorted_words)

ex22.print_first_and_last(sentence)
ex22.print_first_and_last_sorted(sentence)

ex22.break_words(sentence)
