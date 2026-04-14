def bracket_validator(input: str) -> bool:
    stack = []
    close_to_open = {"(": ")", "{": "}", "[": "]"}

    for c in input:
        if c in close_to_open:
            stack.append(c)
        elif c in close_to_open.values():
            if not stack:
                return False
            last_open = stack.pop()
            if c != close_to_open[last_open]:
                return False
    return not stack


print("===========================")

print(bracket_validator("(]"))           # False
print(bracket_validator("([)]"))         # False
print(bracket_validator("((("))          # False
print(bracket_validator("())"))          # False
print(bracket_validator("{[(])}"))       # False
