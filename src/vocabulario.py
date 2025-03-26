
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vocales)
