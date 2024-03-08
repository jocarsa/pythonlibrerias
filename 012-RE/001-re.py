import re

correo = "info@josevicentecarratala.com"
patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

resultado = re.findall(patron, correo)
print(resultado)
