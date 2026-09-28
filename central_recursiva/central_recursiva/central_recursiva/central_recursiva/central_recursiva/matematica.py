def mdc_recursivo(a, b):
    if b == 0:
        return a
    return mdc_recursivo(b, a % b)

def soma_digitos_recursivo(n):
    if n == 0:
        return 0
    return (n % 10) + soma_digitos_recursivo(n // 10)
