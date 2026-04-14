def Pattern_tracker(text):
    
    i = 0
    counter = 0
    while i < len(text):
        if text[i].isdigit():
            if text[i-1].isdigit() and int(text[i]) == int(text[i - 1]) + 1:
                counter += 1
        i += 1

    return counter


print(Pattern_tracker("123a345"))
print(Pattern_tracker("1a2b3c4d5"))  
print(Pattern_tracker("12asd34hkh45kjhj56jhj67kjhjh78kjhjh89kjhkhj110"))
print(Pattern_tracker(""))          
print(Pattern_tracker("012345"))    

