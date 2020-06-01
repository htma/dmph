import random

class Hash(object):
    def __init__(self, M, N):
        self.M = M # size of existed hash table
        self.N = N # size of expanded hash table is M + N
        self.salt = []

    def __call__(self, key):
        skey = str(key)
        while len(self.salt) < len(skey):
            self.salt.append(random.randint(0, self.N-1))

        return sum(self.salt[i] * ord(c)
                   for i, c in enumerate(skey)) % self.N + self.M

if __name__ == '__main__':
    K1 = ['Elephant', 'Horse', 'Camel', 'Python', 'Dog', 'Cat']
    K2 = ['Ant', 'Fish']

    H1 = [-1]*len(K1)
    H2 = [-1] * len(K2)
    hash1 = Hash(0, len(K1))
    H1 = [hash1(key) for key in K1]
    print(H1)
    hash2 = Hash(max(H1)+1, len(K2))
    H2 = [hash2(key) for key in K2]
    print(H2)


