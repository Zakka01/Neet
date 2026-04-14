def Pattern_tracker(text):
    
    i = 1
    counter = 0
    while i < len(text):
        if text[i].isdigit() and text[i-1].isdigit() :
            if int(text[i]) == int(text[i - 1]) + 1:
                counter += 1
        i += 1

    return counter

print(Pattern_tracker("12 34 45 56 67 78 89 110"))
print(Pattern_tracker("123a345"))
print(Pattern_tracker("012345"))
