def pares_impares(limit):
    """
    Genera números pares e impares en listas separadas hasta un límite dado.

    Args:
      limit: El valor máximo que puede alcanzar un número.

    Returns:
      Una tupla que contiene dos listas: una de números pares y otra de impares.
    """
    pares = []
    impares = []
    num = 1
    while num < limit:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
        num += 1
    yield pares
    yield impares

pares, impares = pares_impares(10)
print("Números pares:", pares)
print("Números impares:", impares)