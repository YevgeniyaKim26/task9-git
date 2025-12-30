def process_numbers():
    n = 0
    s = 0
    m = None

    while True:
        x = int(input("Enter number: "))

        if x == -1:
            break

        if n == 0:
            m = x
        elif x < m:
            m = x

        s = s + x
        n = n + 1

    if n == 0:
        m = -1
        a = -1
    else:
        a = s / n

    print("n =", n)
    print("s =", s)
    print("m =", m)
    print("a =", a)


process_numbers()