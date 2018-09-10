class xorshift(object):
    """
    Xorshift Random Number Generator. Implementação de um algoritmo
    simples para geração de números pseudo-aleatórios.
    """

    """
    Construtor da classe.

    seed (int): semente usada.
    """
    def __init__(self, seed):
        self.last = seed

    """
    Gera um número aleatório.

    m (int) = módulo.
    """
    def generate(self, m):
        self.last ^= (self.last << 21)
        self.last ^= (self.last >> 35)
        self.last ^= (self.last << 4)

        return self.last % (2**m)