import string
import random
//Abril estuvo aqui jeje//
def generate_password(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special_chars=True):
    # Crear lista de caracteres posibles
    chars = []
    if include_uppercase:
        chars.extend(string.ascii_uppercase)
    if include_lowercase:
        chars.extend(string.ascii_lowercase)
    if include_numbers:
        chars.extend(string.digits)
    if include_special_chars:
        chars.extend(string.punctuation)

    # Generar contraseña aleatoria
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Solicitar al usuario la longitud y reglas de complejidad
length = int(input("Escribe cuantos caracteres de la contraseña quieres perro: "))
include_uppercase = input("Incluir letras mayúsculas (S/N)? ").upper() == 'S'
include_lowercase = input("Incluir letras minúsculas (S/N)? ").upper() == 'S'
include_numbers = input("Incluir números (S/N)? ").upper() == 'S'
include_special_chars = input("Incluir caracteres especiales (S/N)? ").upper() == 'S'

# Generar y mostrar la contraseña
password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
print("Contraseña generada AUUUUUUU MEOW MEOW:", password)
