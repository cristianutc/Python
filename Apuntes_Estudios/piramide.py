altura = 5

for i in range(1, altura + 1):
    espacios = altura - i
    estrellas = 2 * i - 1
    print(" " * espacios + "*" * estrellas)