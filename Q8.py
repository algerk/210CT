def n_vowel(text):
    vowel = ["a", "e", "i", "o", "u"]
    char = []

    for v in text:
        if v.lower() not in vowel:
            #makes letters lowercase and takes all letters that arent vowels
            char.append(v)
#appends letters to characters list
    return "".join(char)
#joins letters and returns word with no vowels

