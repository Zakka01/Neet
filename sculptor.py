def sculptor(string):
    s = ""
    i = 0
    flag = True
    
    for char in string:

        if char.isalpha():
            if flag:
                s += char.lower()
            else:
                s += char.upper()
            flag = not flag
        else:
            s += char
    
    return s


print(sculptor("Hello world"))
print(sculptor("123abcDEF"))
print(sculptor("a-bC-dEf-ghIj"))
