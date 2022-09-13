# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:20:36 2022

@author: matep
"""

"""
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje 
con el resultado de la nota y si ha aprobado o no.

English:

Create a program and It needs to have a class called Alumno,as attributes the name and the grade of the student.
Determine the methods to inicialize its attributes, print them and show a message
with the result of the grade if it is approved or not.

"""

#Declare class Alumno with its attributes nombre is an String and nota is an Integer
class Alumno:
    nombre = ""
    nota = 0
        
#Function StudentData with argument(class Alumno, and variable nombre = Nombre_alumno and variable nota = Nota_alumno), in this function we will save the information    
def DatosAlumno (Alumno,Nombre_alumno,Nota_alumno):
        Alumno.nombre = Nombre_alumno
        Alumno.nota = Nota_alumno

#Function recibirDatos will receive information from the user, and that information will be saved in the function DatosAlumno
def recibirDatos (Alumno):
        Nombre_alumno=input("Digitar nombre: ")                         
        Nota_alumno= float(input("Digitar la nota: "))
        print("**********************************")
        DatosAlumno(Alumno,Nombre_alumno,Nota_alumno)
        
#Function calcular_nota, This will be to know if the student approved or no, so if student had a grade less than 3, the student didn't approve, otherwize student approved
def calcular_nota(Alumno):
    if  Alumno.nota < 3:                                                
        print("El estudiante no pasó")
    else:
        print("El estudiante pasó")

#Function mostrarDatos, and here the program will show you all the information saved before, and you'll get the name of the student and its respective message if student approved or not    
def mostrarDatos(Alumno):
        print("Nombre del alumno: ", Alumno.nombre)
        print("Nota del alumno: ", Alumno.nota)
        calcular_nota(Alumno)

#Object estudiante1 will be the instance of the class Alumno() 
estudiante1 = Alumno()
#Message first student data
print("Datos primer estudiante: ")
recibirDatos(estudiante1)
mostrarDatos(estudiante1)

"""
Realizar un programa que tenga una clase Persona con las siguientes características. 
La clase tendrá como atributos el nombre y la edad de una persona. 
Implementar los métodos necesarios para inicializar los atributos, 
mostrar los datos e indicar si la persona es mayor de edad o no.

English:

Create a program with the class called Persona and the following features.
The class will have as attributes the name and age of a person-
Implement the methods required to initialize the attributes,
show the information and indicating if the person is adult or no. 
"""

#Declare the class Persona
class Persona:
    #Constructor Method, variable self.nombre is String and self.edad is an integer variable, Both of them are input variables  
    def __init__(self):
        self.nombre = input("Digitar el nombre: ")
        self.edad = int(input("Digitar su edad: "))
        
    #Function edadmayor, it will give us the message if the person is adult or no, if the age is less or equal of 18 they are not adults, otherwise they are
    def edadmayor(self):
        if self.edad <= 18:
            print("Es menor de edad")
        else:
            print("Es mayor de edad")

    #Function Datopersona, It will show us the information of the person, with their name and age, also the information if they are adults or no.        
    def Datospersona(self):
            print("Nombre de la persona: {}".format(self.nombre))
            print("Edad de la persona: {}".format(self.edad))
            self.edadmayor()

#Object persona1 the instance of class Persona                 
persona1 = Persona()
#Objetc calling the function Datospersona
persona1.Datospersona()

"""
Desarrollar un programa que cargue los datos de un triángulo. 
Implementar una clase con los métodos para inicializar los atributos, 
imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es 
(equilátero, isósceles o escaleno).

English 

Create a program to get the data of a triangle
Implement a class with the methods to initialize the attributes,
print the valor of the side with the highest size and the type ot triangle 
(equilateral,isoceles, scalene)
"""

#Declare class Triangle
class Triangulo:
    
    #Method constuctor with 3 variables as integer type, being the side of a triangle
    def __init__(self):
        self.lado1 = 0
        self.lado2 = 0
        self.lado3 = 0

    #Function registrarvalores, it will be to get the information of the value to each side from the user    
    def registrarvalores(self):
        self.lado1 = int(input("Digite los valores para lado 1: "))
        self.lado2 = int(input("Digite los valores para lado 2: "))
        self.lado3 = int(input("Digite los valores para lado 3: "))
        
    #Function tipodetriangulo, here we'll know what type of the triangle is 
    def tipodetriangulo(self): 
        #If the first side is equal to the second side and first side is equal to the third side will be an equilateral triangle and show us the message    
        if  self.lado1 == self.lado2 and self.lado1 == self.lado3: 
            print("Cumple los parametros para ser un triangulo equilatero")
        #if the first side is different to the second side and first side is different to the third side and the third side is different to the second side, this will be a scalene triangle
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado3 != self.lado2:
            print("Cumple los parámetros para ser un triángulo escalenos")
        #if first side is equal to second side or second side is equal to third side or first side is equal to the third side, this will be a isosceles triangle    
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            print("Cumple los parámetros para ser un triángulos Iscosceles")

    #Function valormayor, it will calculate what size will be the highest        
    def valormayor(self):
        #if first size is higher than second one and third size, the first side will be the highest 
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El valor mayo es: ", str(self.lado1))
        #If second size is higher than the first side and third size, the second side will be the highest
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El valor mayor es: ", str(self.lado2))
        #Otherwise the third size will be the highest side    
        else:
            print("El valor mayor es: ", str(self.lado3))   
              
#Object resultadotriangulo will be the instance of the class Triangulo
resultadotriangulo = Triangulo()
#It's call Function registrarvalores 
resultadotriangulo.registrarvalores()
#It's call function tipodetriangulo
resultadotriangulo.tipodetriangulo()
#It's call function valormayor
resultadotriangulo.valormayor()

print("*******************************************************************************************")
        
"""
Realizar una clase que administre una agenda.
Se debe almacenar para cada contacto el nombre, el teléfono y el email.
Además deberá mostrar un menú con las siguientes opciones.
Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda

English 

Calculate a class to manage a planner
It must store for each contact the name, the phone and email
Also it must show a menu of the following options

Add a contact
List of contact
Look for a contact
Edit a contact 
Close the planner

"""




#Declare the class Agenda
class Agenda:


    #Method costructor with the variable self.contactos is a list, and there is where we are going to save all the data of the contacts
    def __init__(self):
        self.contactos = [] 

  
    #Method menu where it will show the information of what option there is to choose
    def menu(self):
        #The variable menu will show each part of what the menu has
        menu= [
		['Agenda Personal'],
		['1. Añadir Contacto',"anadir"],
		['2. Lista de contactos'],
		['3. Buscar contacto'],
		['4. Editar contacto'],
		['5. Cerrar agenda']
        ]
        
        #As we have 6 differents sentences, we use the cicle for to print each one
        for x in range(6):
            print(menu[x][0])#We print the variable menu, using the results of x and 0 starting in the first sentence
        
        #variable option to know what the user wants to do
        opcion = int(input("Introduzca la opción que desea: "))
        
        #If it is 1, it will go to the function self.añadir
        if opcion == 1:
            self.añadir()

        #if it is 2, it will go to the function self.lista    
        elif opcion == 2:
            self.lista()

        #if it is 3, it will go to the function self.buscar    
        elif opcion == 3:
            self.buscar()
        #if it is 4, it will go to the function self.editar    
        elif opcion == 4:
            self.editar()

        #if it is 5, it will exit of the planner   
        elif opcion == 5:
            print("Saliendo de la agenda...")
            exit()
        self.menu()#and we call the method menu, as soon as we finish to use the option that we used

    #function añadir, here we are going to add new contacts in the list     
    def añadir(self):
        print("______________________")
        print("----Añadir----")
        print("______________________")
        nombre = input("Ingrese el nombre: ")
        telefono = int(input("ingresar el telefono: "))
        email = input("Ingresar el email: ")
        self.contactos.append({'nombre': nombre,'telefono': telefono,'email': email})
        print("Se ha agregado a la lista")


    #Function lista is for show us what contacts we have in the list
    def lista(self):
        print("______________________")
        print("----Lista----")
        print("______________________")
        if not self.contactos:
            print("No tiene contactos")
        else:
            print("Esta es la lista de contactos")
            for contacto in self.contactos:
                print("Datos del contacto: ", contacto)
        print("*******************************************")


    #Function to look for a contact specifically
    def buscar(self):
        print("______________________")
        print("----Lista----")
        print("______________________")
        nombre = str(input("Introduzca el nombre: "))
        for x in range (len(self.contactos)):
            if nombre == self.contactos[x]['nombre']:
                print("Datos del contacto: ")
                print("Nombre: ", self.contactos[x]['nombre'])
                print("Telefeno: ", self.contactos [x]['telefono'])
                print("E-mail: ", self.contactos [x]['email'])
                print("*********************************************")

                return x
            else:
                print("Este contacto no sé encontró")
            
        print("*****************************************************")

    #Function to edit a contact in the list    
    def editar(self):
        print("--------------------------------------")
        print("Editar contacto")
        print("--------------------------------------")
        data =self.buscar() # variable data will be the x that we have in the cycle for in the function buscar
        condition = False
        while condition == False:
            print("Seleccionar que quieres editar: ")
            print("1. Nombre")
            print("2. Teléfono")
            print("3. E-mail")
            print("4. volver")
            option = int(input("Introduzca la opción deseada: "))
            if option == 1:
                nombre=input("Introduzca el nuevo nombre: ")
                self.contactos[data]['nombre']=nombre
            elif option == 2:
                telefono=input("Introduzca el nuevo telefono: ")
                self.contactos[data]['telefono']=telefono
            elif option == 3:
                email=input("Introduzca el nuevo email: ")
                self.contactos[data]['email']=email
            elif option == 4:
                condition = True


#object agenda1 will be the instance of the class Agenda 
agenda1 = Agenda()
#We call the function menu to start our planner
agenda1.menu ()

