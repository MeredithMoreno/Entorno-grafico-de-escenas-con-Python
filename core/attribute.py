from OpenGL.GL import * 
import numpy

class Attribute(object):
    def __init__(self, dataType, data):
        #Tipo de elemnetos en la memoria del array
        #int| float | vc2 | vec3 | vec4
        self.dataType = dataType
        #Arreglo de memoria que sera almacenada en el buffer
        self.data = data

        #Referencia a un buffer disponible en GPU
        self.bufferRef = glGenBuffers(1)

        #caragadr datos inmediatamnete
        self.uploadData()
    
    #cargar esos datos al buffer de la GPU 
    def uploadData(self):
    
        #Convertir datos a formato de arreglo de numpy, convertor en flotantes
        data = numpy.array(self.data).astype(numpy.float32)
        
        #Seleccionar el buffer usado por las sigueintes funciones  
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        #Alamecnar los datos y al buffer enlazado
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    #Asociar variables en el programa de la gpu con este buffer  
    def associateVariable(self, programRef, variableName ):
        
        #Obtener referencias para la varibal del prgrama con un nombre dado
        variableRef = glGetAttribLocation(programRef, variableName)

        #si el programa noreferncia la varble, salir 
        if variableRef == -1:
            return
        #Seleccionar el buffer usado para la funcion siguiente
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        #Especificar como los datos seran leidos dsde el buffer actualmente vinculado

        if self.dataType == "int":
            glVertexAttribPointer(variableRef, 1, GL_INT, False, 0, None)
        elif self.dataType == "float":
            glVertexAttribPointer(variableRef, 1, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec2":
            glVertexAttribPointer(variableRef, 2, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableRef, 3, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec4":
            glVertexAttribPointer(variableRef, 4, GL_FLOAT, False, 0, None)
        else:
            #raise Exception("Tipo de dato desconocido"+self.data)  
            raise Exception("Attribute " + variableName + " has unknown type "+ self.dataType)  
        
        #indicar dato fue feuerin transmitidos al buffer
        glEnableVertexAttribArray(variableRef)
    




