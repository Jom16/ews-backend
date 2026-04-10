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

# Funciones
def saludar(nombre):
    print(f"Hola, {nombre}. Bienvenido al path de Backend Engineering.")

saludar("Luis")
saludar("Wewa")

# Funciones con retorno
def sumar(a, b):
    return a + b

resultado = sumar(10, 5)
print(resultado)
print(sumar(100, 200))

# Funciones con return — ejemplo cafe
def precio_cafe():
    return 80

def total_con_propina(precio):
    return precio + (precio * 0.10)

cafe = precio_cafe()
total = total_con_propina(cafe)
print(f"Total a pagar: {total} pesos")

# Funciones con logica real
def clasificar_servidor(uso_cpu):
    if uso_cpu >= 90:
        return "ALERTA CRITICA!"
    elif uso_cpu >= 70:
        return "ALERTA WARNING"
    else:
        return "NORMAL"

print(clasificar_servidor(95))
print(clasificar_servidor(75))
print(clasificar_servidor(40))

# OOP - Clases y objetos
class Servidor:
    def __init__(self, nombre, ip, estado):
        self.nombre = nombre
        self.ip = ip
        self.estado = estado

    def mostrar_info(self):
        return f"{self.nombre} | IP:  {self.ip} | Estado: {self.estado}"
    
servidor1 = Servidor("NOC-01", "192.168.1.1", "ACTIVO")
servidor2 = Servidor("NOC-02", "192.168.1.2", "CRITICO")

print(servidor1.mostrar_info())
print(servidor2.mostrar_info())