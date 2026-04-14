def convert_base(num: str, from_base: int, to_base: int) -> str:
    bases = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not 2 <= from_base <= 36:
        return "ERROR"
    if not 2 <= to_base <= 36:
        return "ERROR"

    try:
        number = int(num, from_base)
    except ValueError:
        print("ERROR")
        exit(0)

    list_int = []
    while number > 0:
        list_int.append(bases[number % to_base])
        number = number // to_base

    list_int.reverse()
    result = "".join(list_int)
    print(result)


convert_base("10", 10, 2)
convert_base("26", 10, 16)
convert_base("46655", 10, 36)
# convert_base("1F4", 16, 10)
convert_base("2", 2, 10)
convert_base("G", 16, 10)
