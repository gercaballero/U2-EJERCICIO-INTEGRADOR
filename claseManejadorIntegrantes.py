from claseIntegrantes import Integrante
import csv
class ManejadorIntegrantes:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def agregarIntegrante(self,unIntegrante):
        self.__lista.append(unIntegrante)
    def test(self):                         #CARGA LOS INTEGRANTES DEL ARCHIVO INTEGRANTESPROYECTO.CSV
        archivo=open('integrantesProyecto.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera = not bandera       #SALTEA LA CABECERA
            else:
                unIntegrante=Integrante(str(fila[0]),str(fila[1]),int(fila[2]),str(fila[3]),str(fila[4]))
                self.agregarIntegrante(unIntegrante)
        archivo.close()

    def listar(self):               #MUESTRA LOS OBJETOS DE LA LISTA
        for integrante in self.__lista:
            integrante.mostrar()
 
    def buscarIntegrantes(self,idProyecto):             #CUENTA LOS INTEGRANTES CON ROL INTEGRANTE
        cont=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getId()==idProyecto and self.__lista[i].getRol()=='integrante':
                    cont=cont+1
        return cont
    
    def buscarDirecCateg(self,idProyecto):  #BUSCA DIRECTOR CON CATEG I O II
        band=True
        i=0
        while band and i<len(self.__lista):
            if self.__lista[i].getId()==idProyecto and self.__lista[i].getRol()=='director' and self.__lista[i].getCat() in ('I','II'):
                    band=False
            else:
                i=i+1
        return band
    def buscarCoDirecCateg(self,idProyecto): #BUSCA CODIRECTOR CON CATEG I O II O III
        band=True
        i=0
        while band and i<len(self.__lista):
            if self.__lista[i].getId()==idProyecto and self.__lista[i].getRol()=='codirector' and self.__lista[i].getCat() in ('I','II','III'):
                        band=False
            else:
                i=i+1
        return band
    def buscarDir(self,idProyecto): #BUSCA SI EXISTE DIRECTOR PARA UN ID DE PROYECTO
        band=True
        i=0
        while band and i<len(self.__lista):
            if self.__lista[i].getId()==idProyecto and self.__lista[i].getRol()=='director':
                        band=False
            else:
                i=i+1
        return band
    def buscarCoDir(self,idProyecto):   #BUSCA SI EXISTE CODIRECTOR PARA UN ID DE PROYECTO
        band=True
        i=0
        while band and i<len(self.__lista):
            if self.__lista[i].getId()==idProyecto and self.__lista[i].getRol()=='codirector':
                        band=False
            else:
                i=i+1
        return band