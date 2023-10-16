from OpenGL.GL import *
# static methods to load and compile OpenGL shaders and link to create programs

class OpenGLUtils(object):
    @staticmethod
    def initializeShader(shaderCode, shaderType):
        """
        Inicializa y compila un shader OpenGL.

        Args:
            shaderCode (str): Código fuente del shader.
            shaderType (int): Tipo de shader (GL_VERTEX_SHADER o GL_FRAGMENT_SHADER).

        Returns:
            int: Referencia al shader compilado.
        """
        #Especificar OpenGl version y requerimientos
        shaderCode='#version 330\n' + shaderCode
        

        #Crear el objeto shader vacio y regresar el valor de referencia 
        shaderRef=glCreateShader(shaderType)

        #Almacenar el codigo fuente en el shader
        glShaderSource(shaderRef,shaderCode)

        #Compilar el codigo fuente que esta almacenado en el shader
        glCompileShader(shaderRef)

        #   Solicitud si la compilacion fue exitosa
        compileSuccess = glGetShaderiv(shaderRef,GL_COMPILE_STATUS)
        
        if not compileSuccess:
            #Regresa mensaje de error
            errorMessage = glGetShaderInfoLog(shaderRef)
           
            #Liberar el uso de la memoria del programa del shader
            glDeleteShader(shaderRef)
           
            #Covertir byte string a un arreglo de caracteres
            errorMessage = '\n' + errorMessage.decode('utf-8')
           
            #Generar una exception, almacena el programa y enviara una mensaje de error
            raise Exception( errorMessage )  
        
        #Compilacion fue exitosa
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        """
        Inicializa y enlaza un programa OpenGL con shaders compilados.

        Args:
            vertexShaderCode (str): Código fuente del shader de vértices.
            fragmentShaderCode (str): Código fuente del shader de fragmentos.

        Returns:
            int: Referencia al programa enlazado.
        """
        #compila shaders y almacena referencias 
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)

        #crear objeto programa y referencia de alamacenamiento
        programRef = glCreateProgram()
        
        #Adjuntar shaders previamente compilados 
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)
        
        #Vincular vertice con fragmento
        glLinkProgram(programRef)

        #consultar si el enlace fue  exitoso
        linkSuccess = glGetProgramiv(programRef,GL_LINK_STATUS)
        
        if not linkSuccess:
            #Recuperar el mensaje de error
            errorMessage=glGetProgramInfoLog(programRef)
            
            #Congelar memoria usada para alamacenar el programa
            glDeleteProgram(programRef)
            
            #convertir arreglo de bytes a arreglo de caracteres 
            errorMessage='\n' + errorMessage.decode('utf-8')
            
            #Generamos una exepcion que detiene el programa y envia un mensaje de error
            raise Exception(errorMessage)     
            
            #Vinculacion fue exitosa, regresa la referencia del programa
        return programRef  
    
    @staticmethod 
    def printSystemInfo(): 
        """
        Imprime información del sistema relacionada con OpenGL.

        Returns:
            None
        """
        print(" Vendor: " + glGetString(GL_VENDOR). decode('utf-8') ) 
        print("Renderer: " + glGetString(GL_RENDERER). decode('utf-8') )
        print("OpenGL version supported: " + glGetString(GL_VERSION).decode('utf-8') )
        print(" GLSL version supported: " + glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8') )

   






































