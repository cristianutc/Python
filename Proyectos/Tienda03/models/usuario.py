import bcrypt
from db.connection import Database

class Usuario:
    """
    Nueva clase Usuario:
    -Maneja registros y login de usuarios
    _Implementa hash seguro con bcrypt
    """

    def __init__(self, db: Database):
        self.db = db

    # Genera hash de contraseña
    def has_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()
    
    # Verifica contraseña contra hash
    def check_password(self, password, hashed):
        return bcrypt.checkpw(password.encode(), hashed.encode())
    
    # Registro de usuario
    def registrar(self, nombre, edad, correo, password):
        with self.db.connect() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM usuarios WHERE correo_electronico=%s", (correo,))
            if cur.fetchone():
                print("Correo ya Registrado.")
                return False
            password_hash = self.has_password(password)
            cur.execute(
                "INSERT INTO usuarios (nombre, edad, correo_electronico, password) VALUES ( %s, %s, %s, %s)",
                (nombre, edad, correo, password_hash)
            )
            print("Usuario resgistrado.")
            return True
    
    #Login de Usuario
    def login(self, correo, password):
        with self.db.connect() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM usuarios WHERE correo_electronico=%s", (correo,))
            Usuario = cur.fetchone()
            if Usuario and self.check_password(password, Usuario[4]):
                print("Login Exitoso")
                return True
            else:
                print("Usuario o contraseña incorrectos")
                return False