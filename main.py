from claseManejadorProyecto import ManejadorProyecto
from claseManejadorIntegrantes import ManejadorIntegrantes
import os

if __name__=='__main__':
    mp=ManejadorProyecto()      #OBJETO MANEJADOR DE PROYECTOS
    mi=ManejadorIntegrantes()   #OBJETO MANEJADOR DE INTEGRANTES
    mp.test()                   #SE CARGAN LOS PROYECTOS DESDE EL ARCHIVO
    mi.test()                   #SE CARGAN LOS INTEGRANTES DESDE EL ARCHIVO
    print('\t\t -------INTEGRANTES DE LOS PROYECTOS-------')                
    mi.listar()                 #LISTAR INTEGRANTES
    input()                     
    os.system('cls')
    print('\t --------PROYECTOS SIN REGLAS APLICADAS---------')  
    mp.listar()                 #LISTAR PROYECTOS SIN PUNTAJES    
    print('\t ------------------------------') 
    input()
    os.system('cls')
    mp.puntaje(mi)              #SE CALCULAN LOS PUNTAJES DE LOS PROYECTOS SEGUN LAS REGLAS
    os.system('cls')
    print('\t --------PROYECTOS CON REGLAS APLICADAS---------')  
    mp.listar()                 #LISTAR PROYECTOS CON PUNTAJES ORDENADOS CON LAS REGLAS APLICADAS
    print('\t ------------------------------') 
    input()
       


