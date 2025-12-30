def largest_square(n):
    i = 0

    while (i * i) <= n:
        i = i + 1

    q = (i - 1) * (i - 1)
    return q


n = 31
q = largest_square(n)
print("Largest square less than or equal to", n, "is", q)
# it looks like I learned how to use git today
