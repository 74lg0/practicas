# Implementacion de cifrado con Fernet
# Autor: 74lg0

# Importacion de Fernet mediante cryptography
from cryptography.fernet import Fernet

# PyStyle para dar estilo a la salida
from pystyle import Colorate, Colors, Box

# Implementamos el titulo
print(Colorate.Horizontal(Colors.red_to_blue, Box.Lines("Implementacion de cifrado con Fernet")))

# Generacion de la clave Fernet
key = Fernet.generate_key()

# Generamos la clase para encriptar
f = Fernet(key)

# Entrada con el texto a cifrar
texto_to_cipher = input(Colorate.Horizontal(Colors.green_to_blue, "\nIngresa el texto a encriptar -> "))

# Proceso de encriptacion
# Ecriptamos el mensaje
texto_cipher = f.encrypt(texto_to_cipher.encode('utf-8'))

# Mostramos los datos

# Variable para almacenar los datos
data = f"""
data = (
    key = [{key.decode('utf-8')}],
    encripted_message = [{texto_cipher.decode('utf-8')}]
)
"""

# Imprimimos los datos
print(Colorate.Horizontal(Colors.rainbow, data))

# Opcionalmente los guardamos
with open('data.txt', 'w') as file:
    file.write(data)