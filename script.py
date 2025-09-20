# Crear estructura completa de proyecto web para "La Tienda - Personajes"
import os

# Crear estructura de directorios
directories = [
    "personajes-la-tienda",
    "personajes-la-tienda/assets",
    "personajes-la-tienda/assets/css",
    "personajes-la-tienda/assets/js",
    "personajes-la-tienda/assets/img"
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

print("📁 Estructura de directorios creada:")
for directory in directories:
    print(f"   {directory}")