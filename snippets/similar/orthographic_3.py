def function(string):
    words1 = ""
    words2 = ""
    for word in string.split():
        if word[0] in ["a", "e", "i", "o", "u", "y"]:
            words1 = words1 + word + " "
        else:
            words2 = words2 + word + " "

    return words1, words2
