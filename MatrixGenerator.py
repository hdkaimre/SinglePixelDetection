__author__ = 'Hans Daniel Kaimre'

from scipy.linalg import hadamard

n = int(input("Sisesta maatriksi m66de(peab olema 2 aste):"))
hadamard = hadamard(n)

print(hadamard)
