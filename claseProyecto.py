class Proyecto:
    __id=''
    __titulo=''
    __palabrasClave=''
    __puntaje=100   #LOS PROYECTOS TIENEN UN PUNTAJE INICIAL DE 100

    def __init__(self,id,titulo,pClaves,puntaje=100): #LOS PROYECTOS TIENEN UN PUNTAJE INICIAL DE 100
        #SE VERIFICA LOS TIPOS DE DATOS
        if isinstance(id, str) and isinstance(titulo, str) and isinstance(pClaves, str) and isinstance(puntaje, int):
            self.__id=id
            self.__titulo=titulo
            self.__palabrasClave=pClaves
            self.__puntaje=puntaje
    def mostrar(self):
        print('ID:{}\nTITULO:{}\nPALABRAS CLAVE:{}\nPUNTAJE:{}\n'.format(self.__id,self.__titulo,self.__palabrasClave,self.__puntaje))
    def getId(self):            #RETORNA ID
        return str(self.__id)
    def getPuntaje(self):       #RETORNA PUNTAJE
        return int(self.__puntaje)
    def puntaje(self,puntos):           #ACUMULA EL PUNTAJE QUE RECIBE COMO PARAMETRO
        self.__puntaje=self.__puntaje+puntos
    def __gt__(self,otro):
        if type(otro)==Proyecto:
          return (self.getPuntaje()>otro.getPuntaje())
