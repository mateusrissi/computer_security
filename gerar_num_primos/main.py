import time
from lcg import LCG
from Fermat import Fermat
from MillerRabin import MillerRabin
from xorshift import xorshift


if __name__ == '__main__':
    """
    Funcao para gerar numeros primos
    """
    n_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    n_bits_len = len(n_bits)

    lcg = LCG(16807)  # seed LCG
    xshif = xorshift(6504)  # seed xorshift
    miller = MillerRabin(5)  # 5 iteracoes
    fermat = Fermat(5)  # 5 iteracoes

    # testanto LCG - MillerRabin
    print("Gerando possiveis primos LCG - MillerRabin\n")
    lcg_miller_start_time = time.time()

    for i in range(0, n_bits_len):
        while True:
            n_primo = lcg.generate(1103515245, 12345, n_bits[i])
            if miller.test(n_primo):
                print("Possível número primo ", n_primo, " de tamanho ", n_bits[i], " bits gerado em ",
                      (time.time() - lcg_miller_start_time), "segundos.")
                break

    lcg_miller_end_time = time.time() - lcg_miller_start_time
    print("--- Tempo de execucao: %s segundos. --- \n" % lcg_miller_end_time)

    # testando LCG - Fermat
    print("Gerando possiveis primos LCG - Fermat\n")
    lcg_fermat_start_time = time.time()

    for i in range(0, n_bits_len):
        while True:
            n_primo = lcg.generate(1103515245, 12345, n_bits[i])
            if fermat.test(n_primo):
                print("Possível número primo ", n_primo, " de tamanho ", n_bits[i], " bits gerado em ",
                      (time.time() - lcg_fermat_start_time), "segundos.")
                break

    lcg_fermat_end_time = time.time() - lcg_fermat_start_time
    print("--- Tempo de execucao: %s segundos. --- \n" % lcg_fermat_end_time)

    # testando xorshift - MillerRabin
    print("Gerando possiveis primos xorshift - MillerRabin\n")
    xorshift_miller_start_time = time.time()

    for i in range(0, n_bits_len):
        while True:
            n_primo = xshif.generate(n_bits[i])
            if miller.test(n_primo):
                print("Possível número primo ", n_primo, " de tamanho ", n_bits[i], " bits gerado em ",
                      (time.time() - xorshift_miller_start_time), "segundos.")
                break

    xorshift_miller_end_time = time.time() - xorshift_miller_start_time
    print("--- Tempo de execucao: %s segundos. --- \n" % xorshift_miller_end_time)

    # testando xorshift - Fermat
    print("Gerando possiveis primos xorshift - Fermat\n")
    xorshift_fermat_start_time = time.time()

    for i in range(0, n_bits_len):
        while True:
            n_primo = xshif.generate(n_bits[i])
            if fermat.test(n_primo):
                print("Possível número primo ", n_primo, " de tamanho ", n_bits[i], " bits gerado em ",
                      (time.time() - xorshift_fermat_start_time), "segundos.")
                break

    xorshift_fermat_end_time = time.time() - xorshift_fermat_start_time
    print("--- Tempo de execucao: %s segundos. --- \n" % xorshift_fermat_end_time)

    print("Programa finalizado com êxito")
