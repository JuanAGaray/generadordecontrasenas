import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input('Dime la longitud de la contrasena'))

new_password = ''

for i in range(longitud):
    new_password = new_password + random.choice(caracteres)

print('La contrasena generada es', new_password)
