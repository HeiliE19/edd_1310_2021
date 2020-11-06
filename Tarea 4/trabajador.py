class Trabajador:
    def __init__( self, num, nom, pat, mat, he, sb, ai ):
        self.__numero_trabajador = num
        self.__nombre = nom
        self.__paterno = pat
        self.__materno = mat
        self.__horas_extra = he
        self.__sueldo_base = sb
        self.__anio_ingreso = ai

    def set_numero_trabajador (self,num):
        self.__numero_trabajador = num

    def get_numero_trabajador (self):
        return self.__numero_trabajador

    def set_nombre (self,nom):
        self.__nombre = nom

    def get_nombre (self):
        return self.__nombre

    def set_paterno (self,pat):
        self.__paterno = pat

    def get_paterno (self):
        return self.__paterno

    def set_materno (self,pat):
        self.__materno = mat

    def get_materno(self, mat):
        return self.__materno

    def set_horas_extra (self,he):
        self.__horas_extra = he

    def get_horas_extra(self):
        return self.__no_cuenta

    def set_sueldo_base (self,sb):
        self.__sueldo_base = sb

    def get_sueldo_base(self):
        return self.__sueldo_base

    def set_anio_ingreso (self,ai):
        self.__anio_ingreso = ai

    def get_anio_ingreso(self):
        return self.__anio_ingreso

    def sueldo():
        print('')

    def mayor_antiguedad():
        print('')

    def menor_antiguedad():
        print('')

    def __str__(self):
        return f"Número de trabajador: {self.__num_trabajador}, Nombre: {self.__nombre}, Paterno: {self.__paterno}, Materno {self.__materno}, Horas extra: {self.__horas_extra}, Sueldo base: {self.__sueldo_base}, Año de ingreso: {self.__anio_ingreso}"
