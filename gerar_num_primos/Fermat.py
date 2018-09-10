import random


class Fermat(object):
    """
    Implementacao do algortimo de Fermat para verificar a primalidade de dado numero.
    """

    """
    Construtor da classe.

    i (int): numero de iteracoes que serao realizadas
    """
    def __init__(self, i):
        self.i = i

    """
    Testa a primalidade de dado numero

    n (int): numero que tera sua primalidade testada
    """
    def test(self, n):
        if n % 2 == 0:
            if n == 2:
                return True
            return False

        for i in range(self.i):
            a = random.randint(1, n - 1)
            return pow(a, n - 1, n) == 1
