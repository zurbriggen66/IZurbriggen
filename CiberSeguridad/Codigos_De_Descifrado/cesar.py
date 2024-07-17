from langdetect import detect
import string

ALFABETO = string.ascii_lowercase

def algoritmo_descifrado(texto_cifrado, clave_descifrado):
    """La funcion descifra texto cifrado a partir de una clave, que fue cifrada con codigo cesar"""

    texto_plano = ""
    for letra in texto_cifrado:
        if letra not in ALFABETO:
            texto_plano += letra
        else:
            indice_letra_cifrada = ALFABETO.index(letra)
            indice_letra_descifrada = indice_letra_cifrada - clave_descifrado
            texto_plano += ALFABETO[indice_letra_descifrada]
    return texto_plano


def fuerza_bruta(texto_cifrado):
    """Esta funcion descifra el cifrado cesar utilizando fuerza bruta"""
    espacio_claves = range(len(ALFABETO))
    for clave in espacio_claves:
        texto_plano = algoritmo_descifrado(texto_cifrado, clave)
        lenguaje = detect(texto_plano)
        if lenguaje == "es":
            print(f"El texto descifrado es: {texto_plano}")
            print(f"La clave de descifrado es: {clave}")


if __name__ == "__main__":

    """Leemos el texto cifrado"""
    texto_cifrado = input("Ingrese el texto cifrado: ").lower()

    """Leemos clave de descifrado"""
    clave_descifrado = int(input("Ingrese clave(numerica): "))

    texto_plano = algoritmo_descifrado(texto_cifrado, clave_descifrado)

    print(texto_plano)
