class LCG(object):
    """
    Linear Congruential Generator (LCG). Implementação de um algoritmo
    simples para geração de números pseudo-aleatórios.
    """
    """
    Construtor da classe.

    seed (int): semente usada. É recomendado que seja um número primo.
    """
    def __init__(self, seed):
        self.seed = seed
        return

    """
    Gera um número pseudo-aleatório.

    a (int): multiplicador.
    c (int): incremento.
    m (int): módulo.
    """
    def generate(self, a, c, m):
        self.seed = (a * self.seed + c) % (2**m)
        return self.seed