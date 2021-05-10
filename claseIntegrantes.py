
class Integrante:
    __idProyecto=''
    __nya=''
    __dni=0
    __categoria=''
    __rol=''

    def __init__(self,id,nya,dni,categ,rol):
        if isinstance(id, str) and isinstance(nya, str) and isinstance(dni, int) and isinstance(categ, str) and isinstance(rol, str):
            self.__idProyecto=id
            self.__nya=nya
            self.__dni=dni
            self.__categoria=categ
            self.__rol=rol
    def mostrar(self):
        print('ID:{}\tN Y A:{:>20}\tDNI:{}\tCATEGORIA:{}\tROL:{}\t'.format(self.__idProyecto,self.__nya,self.__dni,self.__categoria,self.__rol))
    def getId(self):
        return self.__idProyecto
    def getRol(self):
        return str(self.__rol)
    def getCat(self):
        return str(self.__categoria)