def fibonacci(n):
    sequence = [0]
    if n >= 1:
        sequence.append(1)
    for i in range(2, n):
        f = sequence[i - 1] + sequence[i - 2]
        sequence.append(f)

    return sequence


n = int(input("Value: "))
f = fibonacci(n)
print(f"Answer: {f[n - 1] + f[n - 2]}\nSequence: {f}")
