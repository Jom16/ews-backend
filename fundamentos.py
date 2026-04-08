# Variables y tipos de datos

nombre = "Luis"
edad = 30
altura = 1.75
es_backend_engineer = False

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_backend_engineer))

# Listas
habilidades = ["Python", "Git", "GitHub", "Terminal"]
print(habilidades)
print(habilidades[0])
print(habilidades[3])
print(len(habilidades))

# Diccionarios
habilidades.append("FastAPI")
print(habilidades)

habilidades.remove("Terminal")
print(habilidades)

print(len(habilidades))

ingeniero = {
    "nombre": "Luis",
    "edad": 30,
    "lenguaje": "Python",
    "meta": "Ser un profesional en Backend Engineering"
}

ingeniero["lenguaje"] = "Python & FastAPI"
ingeniero["ciudad"] = "Mexico City"

print(ingeniero)
print(ingeniero["lenguaje"])
print(ingeniero["meta"])
print(ingeniero)

# Tuplas
coordenadas = (19.4326, -99.1332)
print(coordenadas)
print(coordenadas[0])
print(type(coordenadas))

# Sets
tecnologias = {"Python", "FastAPI", "Python", "Docker", "FastAPI"}
print(tecnologias)
print(type(tecnologias))