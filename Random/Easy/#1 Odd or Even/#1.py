def even_or_odd(x):
    if x % 2 == 0:
        return "Even"

    return "Odd"

while True:
    try:
        x = int(input("Value: "))
        print(even_or_odd(x))
        break
    except ValueError:
        print("Not a valid value.")
