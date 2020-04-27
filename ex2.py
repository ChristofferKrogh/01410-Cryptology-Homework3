import random
import math

class El_Gamal:
    def __init__(self, p):
        self.p = p
        q = int((p - 1) / 2)
        self.alpha = self.find_primitive(self.p, q)
        # Randomly choose the private key a from Z_{p-1}
        # TODO: should a just be chosen at random???
        self.a = random.randint(2, self.p - 2)
        # beta = alpha ** a % p
        self.beta = pow(self.alpha, self.a, self.p)

    def Hash(self, m):
        n = 2051152801041163
        # 8 ** m & n
        return pow(8, m, n)

    def is_primitive(self, alpha, p ,q):
        # (alpha ** q) % p
        return pow(alpha, q, p) != 1 and pow(alpha, 2, p) != 1

    def find_primitive(self, p, q):
        alpha = 2
        while not self.is_primitive(alpha, p, q):
            alpha += 1

        return alpha

    def signature(self, m):
        k = 1234567
        gamma = pow(self.alpha, k, self.p)
        x = self.Hash(m)
        delta = (x - self.a * gamma)*(1/k) % (self.p - 1)
        return (gamma, delta)

    def verify(self, gamma, delta, m):
        x = self.Hash(m)

        lhs1 = pow(self.beta, gamma, self.p)
        lhs2 = pow(gamma, delta, self.p)
        lhs = lhs1 * lhs2
        print(f"lhs: {lhs}")

        rhs = pow(self.alpha, x, self.p)
        print(f"rhs: {rhs}")

        return lhs == rhs


def main():
    # Exercise 3.2.2
    print("Exercise 3.2.2")
    p = 2189284635404723
    el_gamal = El_Gamal(p)
    print(f" alpha: {el_gamal.alpha}\n a: {el_gamal.a}\n beta: {el_gamal.beta}")

    # Exercise 3.2.3
    print("\nExercise 3.2.3")
    m = 163959
    gamma, delta = el_gamal.signature(m)
    print(f"Signature: {(gamma, delta)}")
    print(f"Is signature verified? {el_gamal.verify(int(gamma), int(delta), m)}")



if __name__ == "__main__":
    main()