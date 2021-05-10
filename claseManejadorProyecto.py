from claseProyecto import Proyecto
from claseManejadorIntegrantes import ManejadorIntegrantes
import csv
import os
class ManejadorProyecto:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def agregarProyecto(self,unProyecto):
        self.__lista.append(unProyecto)         #AÑADE LOS OBJETOS PROYECTO A LA LISTA
    
    def test(self):                         #CARGA LOS PROYECTOS DEL ARCHIVO
        archivo=open('proyectos.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                #SALTEA LA CABECERA
                bandera = not bandera         
            else:
                unProyecto=Proyecto(str(fila[0]),str(fila[1]),str(fila[2]))
                self.agregarProyecto(unProyecto)
        archivo.close()
    
    def listar(self):                               #MUESTRA LOS OBJETOS DE LA LISTA
        self.__lista.sort(reverse=True)             #ORDENA LA LISTA DE MAYOR A MENOR
        for proyecto in self.__lista:
            proyecto.mostrar()

    def reglaA(self,mi,proyecto):
        if mi.buscarIntegrantes(proyecto.getId())>=3:      #SI LOS INTEGRANTES SON MINIMO 3
            retorna='El Proyecto tiene como mínimo 3 integrantes- PUNTAJE +10'
            proyecto.puntaje(10)
        else:
            proyecto.puntaje(-20)
            retorna='El Proyecto debe tener como mínimo 3 integrantes- PUNTAJE -20'
        print('REGLA A----> {}'.format(retorna))

    def reglaB(self,mi,proyecto): 
        if not mi.buscarDirecCateg(proyecto.getId()):#SI ENCUENTRA UN DIRECTOR CON CATEGORIA I O II RETORNA FALSE
            retorna='El Director del Proyecto tiene categoria I o II- PUNTAJE +10'
            proyecto.puntaje(10)
        else:
            retorna='El Director del Proyecto debe tener categoria I o II- PUNTAJE -5'
            proyecto.puntaje(-5)
        print('REGLA B----> {}'.format(retorna))
    
    def reglaC(self,mi,proyecto):
        if not mi.buscarCoDirecCateg(proyecto.getId()):#SI ENCUENTRA UN CODIRECTOR CON CATEGORIA I,IIoII RETORNA FALSE 
            retorna='El Codirector del Proyecto tiene como mínimo categoría III- PUNTAJE +10'
            proyecto.puntaje(10)
        else:
            retorna='El Codirector del Proyecto debe tener como mínimo categoría III- PUNTAJE -5'
            proyecto.puntaje(-5)
        print('REGLA C----> {}'.format(retorna))
    
    def reglaD(self,mi,proyecto): 
        if not mi.buscarDir(proyecto.getId()):#SI ENCUENTRA UN DIRECTOR RETORNA FALSE
            retorna='El Proyecto Tiene un Director'
        else:
            retorna='El Proyecto debe tener un Directo- PUNTAJE -10'
            proyecto.puntaje(-10)
        print('REGLA D----> {}'.format(retorna))
    
    def reglaE(self,mi,proyecto):
        if not mi.buscarCoDir(proyecto.getId()): #SI ENCUENTRA UN CODIRECTOR RETORNA FALSE
            retorna='El Proyecto Tiene un Codirector'
        else:
            retorna='El Proyecto debe tener un Codirector- PUNTAJE -10'
            proyecto.puntaje(-10)
        print('REGLA E----> {}'.format(retorna))

    def puntaje(self,integrantes):
        for proyecto in self.__lista:
            print('\t~~~~PROYECTO ID:{}~~~~'.format(proyecto.getId()))
            #LLAMA A TODAS LAS REGLAS Y ENVIA EL MANEJADOR DE LOS INTEGRANTES Y EL OBJETO PROYECTO
            self.reglaA(integrantes, proyecto)
            self.reglaB(integrantes, proyecto)
            self.reglaC(integrantes, proyecto)
            self.reglaD(integrantes, proyecto)
            self.reglaE(integrantes, proyecto)
            input()
            os.system('cls')




