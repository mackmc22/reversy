def reversy(phrase):
    words = phrase.split(" ")

    backward_phrase = []

    for word in words:
        back_word = ''

        if len(word) >= 5:

            for letter in word:
                back_word = letter + back_word

                if len(back_word) == len(word):
                    backward_phrase.append(back_word)
                    print(back_word)
        else:
            backward_phrase.append(word)

    return backward_phrase


# anything with letters < 5 is not reversed
assert reversy("Welcome to my world") == ["emocleW", "to", "my", "dlrow"]
