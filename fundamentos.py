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

# OOP - Modificar atributos
servidor1.estado = "MANTENIMIENTO"
print(servidor1.mostrar_info())

# OOP - Herencia
class ServidorWeb(Servidor):
    def __init__(self, nombre, ip, estado, dominio):
        super().__init__(nombre, ip, estado)
        self.dominio = dominio

    def mostrar_info(self):
        return f"{self.nombre} | IP:  {self.ip} | Dominio: {self.dominio}"


web1 = ServidorWeb("WEB-01", "192.168.2.1", "ACTIVO", "ews-backend.com")
print(web1.mostrar_info())

# OOP - Encapsulamiento
class ServidorSeguro:
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.__ip = ip  # Atributo privado

    def get_ip(self):
        return self.__ip
    
    def set_ip(self, nueva_ip):
        if "192.168" in nueva_ip:
            self.__ip = nueva_ip
        else:
            return "IP no válida"

seguro1 = ServidorSeguro("SECURE-01", "192.168.3.1")
print(seguro1.get_ip())
seguro1.set_ip("192.168.3.99")
print(seguro1.get_ip())

# OOP — Encapsulamiento | Protegiendo datos como Apple
class iPhone:
    def __init__(self, modelo, color):
        self.modelo = modelo
        self.color = color
        self.__pin = "0000"  # nadie puede tocarlo directamente

    def get_pin(self):
        return "****"  # nunca muestras el pin real

    def set_pin(self, pin_actual, nuevo_pin):
        if pin_actual == self.__pin:
            self.__pin = nuevo_pin
            return "PIN actualizado"
        else:
            return "PIN incorrecto"

mi_iphone = iPhone("iPhone 16 Pro", "Negro")
print(mi_iphone.get_pin())
print(mi_iphone.set_pin("0000", "1234"))
print(mi_iphone.set_pin("9999", "5678"))