# Hash de contraseñas
# Hashear y luego verificar una contraseña es muy sencillo:
import bcrypt 
import binascii

password = b"super secret password"

# Hashear una contraseña por primera vez con un salt aleatorio
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Verificar contraseña
if bcrypt.checkpw(password, hashed):
    print("¡Coincide!")
else:
    print("No coincide :(")

"""KDF (Función de Derivación de Claves)
Desde la versión 3.0.0 bcrypt ofrece una función kdf que implementa bcrypt_pbkdf.
Se usa en el nuevo formato de claves privadas cifradas de OpenSSH."""

key = bcrypt.kdf(
    password=b'password',
    salt=b'salt',
    desired_key_bytes=32,
    rounds=100
)

key2 = bcrypt.kdf(
    password=b'password',
    salt=b'salt',
    desired_key_bytes=32,
    rounds=10
)
print( key == key2)

print("\nClave en bytes:", key)
print("Clave en hexadecimal:", binascii.hexlify(key).decode())
print("Longitud:", len(key))

# Importante
# Para almacenamiento de contraseñas normales:
# Usa hashpw()
# NO uses kdf()

# Para cifrado de datos:
# Usa kdf()