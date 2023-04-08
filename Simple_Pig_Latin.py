def pig_it(text):
    words = text.split()
    pig_latin_words = []
    punctuation = ""

    for word in words:
        hasPunctuation = False
        if word[-1] in ".,!?":
            hasPunctuation = True
            punctuation = word[-1]
            word = word[:-1]
        
        if len(word) == 1:
            pig_latin_words.append(word + punctuation)
            continue

        first_letter = word[0]
        print(first_letter)
        rest_of_word = word[1:]
        pig_latin_word = rest_of_word + first_letter + "ay" + punctuation
        pig_latin_words.append(pig_latin_word)

    pig_latin_text = " ".join(pig_latin_words)      
    return pig_latin_text  
