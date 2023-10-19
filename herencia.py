from enum import Enum
class Persona:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email

    def validar_email(self):
        if "@" in self.email:
            print(f"Correo de activación enviado a {self.email}")


class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, clave_acceso):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email)
        self.clave_acceso = clave_acceso


class Docente(Persona):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email)
        self.cursos_asignados = []


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


class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre


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


class Carrito:
    def __init__(self):
        self.cursos_en_carrito = []

    def agregar_curso(self, curso):
        self.cursos_en_carrito.append(curso)

    def ver_cursos(self):
        return self.cursos_en_carrito


class MedioDePago:
    def __init__(self, tipo):
        self.tipo = tipo

class MedioDeContacto:
    def __init__(self,id_MedioContacto,fecha,email,telefono,direccion,nombre):
        self.id_MedioContacto = id_MedioContacto
        self.fecha = fecha
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.nombre = nombre

class TiposDeMediosDeContacto(Enum):
    whatsapp = MedioDeContacto(1, "","","","","")
    correoelectronico = MedioDeContacto(2,"","","","","")
    CallCenter = MedioDeContacto(3, '', '', '', '', '')
    ReferidoInterno = MedioDeContacto(4, '', '', '', '', '')


""" TiposDeMediosDeContacto.whatsapp.value.fecha = '2023-10-18'

print(TiposDeMediosDeContacto.whatsapp.value.fecha)
print(TiposDeMediosDeContacto.whatsapp.value.id_MedioContacto) """