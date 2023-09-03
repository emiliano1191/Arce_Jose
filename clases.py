""" Ejercicios clases:
1. Crear todas las clases que fueran necesarias para iniciar un proceso de desarrollo de 
software de la siguiente situación:
Una empresa privada que se dedica a la venta de cursos de oficios, desea desarrollar un 
sistema web para poder publicar su oferta académica. Dicho sistema debe mostrar una serie 
de cursos disponibles. 
Por cada curso se deberá visualizar la fecha de comienzo, título, descripción, objetivos, 
programa, costo, duración en meses, foto y estado (disponible o no disponible, en base a su 
estado deberán verse o no en el sitio). A su vez, cada curso pertenece a alguna de las 
siguientes categorías (Inicial, Intermedio, Avanzado). Por otro lado, los cursos contienen un 
conjunto de clases, en donde por cada clase se debe mostrar la fecha, título, contenido, 
URLDrive. 
Cada clase de un curso la dicta un docente, y este puede participar en el dictado de varias 
clases y de varios cursos. De cada docente se desea guardar su apellido, nombre, dni, fecha 
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email. 
Por otra parte, los interesados en inscribirse a un curso deberán crearse una cuenta de usuario 
final, donde deberán registrar su datos personales (nombre, apellido, dni, dirección, fecha 
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email), además de 
confirmar y reconfirmar una clave de acceso. Para la activación de la cuenta de usuario final se 
deberá validar que el email sea verdadero y esté en funcionamiento, enviando un correo 
automático al email registrado. 
Los usuarios públicos registrados pueden inscribirse a uno o más cursos. Además, el sitio 
deberá proveer la posibilidad de registrar 2 roles más de usuarios quienes también tendrán 
interacción con el sistema: Administrador, Docente. Los usuarios también deben tener 
asociado un estado (Activo / Inactivo).
Por último, los usuarios finales podrán agregar uno o más cursos en un carrito de compras, 
donde se deberá visualizar: Foto, título del curso, duración, costo. Una vez confirmados los 
ítems del carrito, deberá seleccionar el medio de pago, los cuales pueden ser: Tarjeta de 
crédito/débito y transferencia bancaria; a fin de tener más datos acerca de los medios de 
pago, deberán registrarse los datos básicos de tarjetas y transferencias). Al confirmar la 
compra, se deberá registrar además la fecha de compra, el usuario que realiza la compra y el 
monto total. Dada la consigna anterior, se pide: identificar, analizar y documentar los 
requisitos según el formato de historias de usuario. Para la creación de las historias, hacer uso 
del repositorio Github, a través de creación de issues """

class Persona:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email, estado="Activo"):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.estado = estado

    def validar_email(self):
        # Lógica de validación de email y envío de correo de activación 
        if "@" in self.email:
            print(f"Correo de activación enviado a {self.email}")


class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email):
        super().__init__(nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email)
    

# Definición de la clase UsuarioFinal 

class UsuarioFinal(Usuario):
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email):
        super().__init__(nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email)
        self.carrito_compras = []

    def agregar_al_carrito(self, curso):
        self.carrito_compras.append(curso)



class Docente(Persona):
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email):
        super().__init__(nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email)


class Administrador(Usuario):
    pass


class Curso:
    def __init__(self, fecha_comienzo, titulo, descripcion, objetivos, programa, costo, duracion_meses, foto, estado, categoria):
        self.fecha_comienzo = fecha_comienzo
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.programa = programa
        self.costo = costo
        self.duracion_meses = duracion_meses
        self.foto = foto
        self.estado = estado
        self.categoria = categoria
        self.clases = []

    def verificar_disponibilidad(self):
        return self.estado == "Disponible"

    def agregar_clase(self, fecha, titulo, contenido, URLDrive):
        clase = Clase(fecha, titulo, contenido, URLDrive)
        self.clases.append(clase)


class Clase:
    def __init__(self, fecha, titulo, contenido, URLDrive):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.URLDrive = URLDrive


class Compra:
    def __init__(self, fecha, usuario, monto_total, cursos_en_carrito, medio_de_pago):
        self.fecha = fecha
        self.usuario = usuario
        self.monto_total = monto_total
        self.cursos_en_carrito = cursos_en_carrito
        self.medio_de_pago = medio_de_pago


class CursoInicial(Curso):
    pass


class CursoIntermedio(Curso):
    pass


class CursoAvanzado(Curso):
    pass


class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre












# intento de uso

# Creación de usuarios
usuario1 = UsuarioFinal("Juan", "Perez", "12345678", "Calle Principal 123", "1990-05-15", "Ciudad", "1234", "Provincia", "1234567890", "juan@example.com")
docente1 = Docente("Maria", "Gonzalez", "98765432", "Calle Secundaria 456", "1985-08-20", "Ciudad", "4321", "Provincia", "9876543210", "maria@example.com")
admin1 = Administrador("Admin", "Admin", "11111111", "Admin Street", "1980-01-01", "Admin City", "0000", "Admin State", "9999999999", "admin@example.com")

# Creación de categorías
categoria1 = Categoria("Inicial")
categoria2 = Categoria("Intermedio")
categoria3 = Categoria("Avanzado")

# Creación de cursos
curso1 = CursoInicial("2023-09-01", "Curso de Python", "Aprende Python con Kevin", "Objetivos del curso", "Programa del curso", 100, 3, "python.jpg", "Disponible", categoria1)
curso2 = CursoIntermedio("2023-09-15", "Curso de SQL", "Aprende SQL avanzado", "Objetivos del curso", "Programa del curso", 120, 4, "sql.jpg", "Disponible", categoria2)
curso3 = CursoAvanzado("2023-10-01", "Curso de Machine Learning", "Aprende ML avanzado", "Objetivos del curso", "Programa del curso", 150, 5, "ml.jpg", "No Disponible", categoria3)

# Agregar cursos al carrito del usuario
usuario1.agregar_al_carrito(curso1)
usuario1.agregar_al_carrito(curso2)

# Compra de cursos
compra1 = Compra("2023-09-02", usuario1, 220, usuario1.carrito_compras, "Tarjeta de Crédito")

# Validar el correo del usuario
usuario1.validar_email()

# Verificar la disponibilidad de un curso
if curso1.verificar_disponibilidad():
    print(f"El curso '{curso1.titulo}' está disponible.")
else:
    print(f"El curso '{curso1.titulo}' no está disponible.")


# Verificar el contenido del carrito antes de comprar
def verificar_carrito(usuario):
    if usuario.carrito_compras:
        print("Contenido del carrito de compras:")
        for curso in usuario.carrito_compras:
            print(f"- {curso.titulo}")
    else:
        print("El carrito de compras está vacío.")

# Mostrar el contenido del carrito de compras antes de comprar
print("Antes de comprar:")
verificar_carrito(usuario1)

# El usuario decide realizar la compra
compra1 = Compra("2023-09-02", usuario1, 220, usuario1.carrito_compras, "Tarjeta de Crédito")

# Vaciar el carrito después de la compra
usuario1.carrito_compras = []

# Mostrar el contenido del carrito de compras después de comprar
print("\nDespués de comprar:")
verificar_carrito(usuario1)






