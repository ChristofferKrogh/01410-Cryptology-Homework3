import random

class El_Gamal:
    def __init__(self, p):
        self.p = p
        q = int((p - 1) / 2)
        self.alpha = self.find_primitive(self.p, q)
        # Randomly choose the private key a from Z_{p-1}
        # TODO: should a just be chosen at random???
        self.a = random.randint(1, self.p - 2)
        # decryption takes a long time with a large private key
        self.a = 2525
        # beta = alpha ** a % p
        self.beta = pow(self.alpha, self.a, self.p)

    def is_primitive(self, alpha, p ,q):
        # pow(alpha, q, p) computes (alpha ** q) % p efficiently
        return pow(alpha, q, p) != 1 and pow(alpha, 2, p) != 1

    def find_primitive(self, p, q):
        alpha = 2
        while not self.is_primitive(alpha, p, q):
            alpha += 1

        return alpha

    def encrypt(self, m, k):
        y1 = pow(self.alpha, k, self.p)
        y2 = pow(m * self.beta, k, self.p)
        return y1, y2

    def decrypt(self, y1, y2):
        return (y2 / (y1 ** self.a)) % self.p

def main():
    # Exercise 3.2.2
    print("Exercise 3.2.2")
    p = 2189284635404723
    el_gamal = El_Gamal(p)
    print(f" alpha: {el_gamal.alpha}\n a: {el_gamal.a}\n beta: {el_gamal.beta}")

    # Exercise 3.2.3
    print("\nExercise 3.2.3")
    m = 163959
    k = 1234567
    # TODO: implement encryption and decryption correctly
    y1, y2 = el_gamal.encrypt(m, k)
    print(f"y1: {y1}, y2: {y2}")
    print(f"Recovered message: {el_gamal.decrypt(y1, y2)}")



if __name__ == "__main__":
    main()