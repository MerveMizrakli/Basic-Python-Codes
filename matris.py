import random

# 5x5'lik matris oluşturma
matrix = [[random.randint(0, 9) for _ in range(5)] for _ in range(5)]

# Matrisi yazdırma
for row in matrix:
    print(row)

