def solve():
    f0 = 1
    f1 = 3
    A = []

    while len(A) < 41:
        if f0 % 2 == 1:
            A.append(f0)

        fn = 5 * f1 + f0
        f0, f1 = f1, fn

    return A[39]

# Выводим ответ
print(solve())
