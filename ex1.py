import math

def find_d(n):
    d = 1
    while math.sqrt(n + d ** 2) % 1 != 0:
        d += 1

    return d


def factor(n):
    # q - p = 2d
    # q * p = n
    # q = 2d + p
    # (2d + p) * p = n
    # => p^2 + 2d*p - n = 0
    # => p = (-2d +- sqrt((2d)^2-4*(-n))) / 2 = -d +- math.sqrt(d**2 + n)

    d = find_d(n)
    p = int(math.sqrt(d**2 + n)) - d
    q = 2*d + p

    print(f"d = {d}")

    return p, q


def main():
    # Exercise 3.1.3
    print("Exercise 3.1.3")
    n = 553190279
    p, q = factor(n)
    print(f"The factors of {n} are {p} and {q}.")

if __name__ == "__main__":
    main()