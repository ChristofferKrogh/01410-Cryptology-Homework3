def euclidsAlgorithm(a, b):
    """
    Euclid's algorithm for computing the greatest common divisor
    """
    a, b = b, a % b
    if b == 0:
        return a
    else:
        return euclidsAlgorithm(a, b)

def gcd(a, b):
    """
    Computes the greatest common divisor of a and b using Euclid's algorithm
    """
    return euclidsAlgorithm(a, b)

def euclidsExtendedAlgorithm(a, b):
    """
    Euclid's extended algorithm, which can be used to compute multiplicative inverses.
    Returns (r, s, t) of gcd(a, b) = r = s * a + t * b
    """
    r = []
    s = []
    t = []
    q = [-1]
    i = 0
    while b != 0:
        r.append(a)
        q.append(int(a / b))
        if i == 0:
            s.append(1)
            t.append(0)
        elif i == 1:
            s.append(0)
            t.append(1)
        else:
            s.append(s[i - 2] - q[i - 1] * s[i - 1])
            t.append(t[i - 2] - q[i - 1] * t[i - 1])

        a, b = b, a % b
        i += 1
    
    r.append(a)
    s.append(s[i - 2] - q[i - 1] * s[i - 1])
    t.append(t[i - 2] - q[i - 1] * t[i - 1])

    return (r[-1], s[-1], t[-1])

def findMultiplicativeInverse(a, b):
    """
    Find the multiplicative inverse of a mod b using Euclid's extended algorithm.
    It is required that a and b are coprime.

    r = s * a + t * b
    r mod b = s * a + t * b mod b
    1 = s * a mod b
    s and a are multiplicative inverse modulo b
    """
    r, s, _ = euclidsExtendedAlgorithm(a, b)
    if r == 1:
        if s < 0:
            return s % b
        else:
            return s
    else:
        return None
    

def main():
    # Exercise 2.1.1

    # Exercise 2.1.2
    # Check that gcd(e, phi(n)) = 1
    print("\nExercise 2.1.2")
    e, p, q = 3, 911, 491
    phi = (p - 1) * (q - 1)
    psi = int(phi / gcd(p - 1, q - 1))

    if gcd(e, phi) == 1:
        print(f"{e} is an allowed exponent!")
    else:
        print(f"{e} is NOT an allowed exponent!")

    print(f"gcd(e, psi(n)) = {gcd(e, psi)}")

    # Exercise 2.1.3
    print("\nExercise 2.1.3")
    print(f"The multiplicative inverse of {e} mod {phi} is {findMultiplicativeInverse(e, phi)}")

    # Exercise 2.1.4
    print("\nExercise 2.1.4")
    print(f"The multiplicative inverse of {e} mod {psi} is {findMultiplicativeInverse(e, psi)}")


if __name__ == '__main__':
    main()