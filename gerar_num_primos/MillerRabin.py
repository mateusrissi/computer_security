import random


class MillerRabin(object):
    """
    Implementação do algoritmo Miller Rabin para a verificacao da primalidade de um dado numero.
    """

    """
    Construtor da classe.

    i (int): numero de iteracoes que o algoritmo ira realizar
    """
    def __init__(self, i):
        self.i = i

    """
    Verifica se 'a' eh um candidato para a composicao de 'n'

    a (int): numero aleatorio onde 1 <= a <= n-1
    d (int): valor de d
    s (int): valor de s
    n (int): numero que ira passar pela tentativa de decomposicao
    """
    def decompose(self, a, d, s, n):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n-1:
                return False
        return True

    """
    Testa a primalidade de dado numero

    n (int): numero que tera sua primalidade testada
    """
    def test(self, n):
        # verifica se n eh par
        if n % 2 == 0:
            if n == 2:
                return True
            return False

        # caso n nao seja primo
        # valores de s e d
        s = 0
        d = n - 1

        while True:
            q, r = divmod(d, 2)
            if r == 1:
                break
            s += 1
            d = q
        assert(2 ** s * d == n - 1)

        for i in range(self.i):
            a = random.randrange(2, n)
            if self.decompose(a, d, s, n):
                return False

        return True