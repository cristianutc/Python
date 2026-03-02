import tkinter as tk
from assets.db import crear_tablas
from assets.interfaz import mostrar_ventana_login

# Crear las tablas si no existen
crear_tablas()

if __name__ == "__main__":
    root = tk.Tk()      # Crear ventana principal
    root.withdraw()     # Ocultarla (porque el login será Toplevel)
    
    mostrar_ventana_login(root)  # Pasar root
    
    root.mainloop()     # Iniciar la aplicación