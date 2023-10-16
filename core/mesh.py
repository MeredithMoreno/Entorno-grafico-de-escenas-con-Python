from core.object3D import Object3D 
from OpenGL.GL import *
import numpy as np

class Mesh(Object3D):

    def __init__(self, geometry, material): 
        """
        Inicializa una instancia de la clase Mesh, que representa un objeto 3D.

        Args:
            geometry (Geometry): La geometría del objeto 3D.
            material (Material): El material que se utilizará para renderizar el objeto.
        """
        super().__init__()
        
        self.geometry = geometry  # La geometría del objeto
        self.material = material  # El material utilizado para renderizar el objeto

        # Determina si este objeto debe ser renderizado
        self.visible = True

        # Configura las asociaciones entre atributos almacenados en la geometría
        # y el programa de sombreado almacenado en el material
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        
        for variableName, attributeObject in geometry.attributes.items():
            attributeObject.associateVariable(material.programRef, variableName)
        
          # Desvincula este objeto de arreglo de vértices (vertex array object)
        glBindVertexArray(0)
        
        