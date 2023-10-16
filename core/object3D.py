from core.matrix import Matrix

class Object3D(object):
    def __init__(self): 
        """
        Inicializa una instancia de la clase Object3D, que representa un objeto tridimensional en una escena.

        La transformación se establece como una matriz de identidad, y el objeto no tiene un padre ni hijos al principio.

        Args:
            No se requieren argumentos específicos para la inicialización.
        """
        self.transform = Matrix.makeIdentity() 
        self.parent = None 
        self.children = []

    def add(self, child):
        """
        Agrega un objeto hijo a este objeto.

        Args:
            child (Object3D): El objeto que se va a agregar como hijo.

        Returns:
            None
        """
        self.children.append(child)
        child.parent = self

    def remove(self, child):
        """
        Elimina un objeto hijo de este objeto.

        Args:
            child (Object3D): El objeto hijo que se va a eliminar.

        Returns:
            None
        """
        self.children.remove(child)
        child.parent = None

    # calculate transformation of this Object3D relative
    # to the root Object3D of the scene graph
    def getWorldMatrix(self):
        """
        Calcula la matriz de transformación de este objeto con respecto al objeto raíz del grafo de escena.

        Returns:
            numpy.ndarray: La matriz de transformación del objeto en coordenadas mundiales.
        """
        if self.parent == None:
            return self.transform
        else:
            return self.parent.getWorldMatrix() @ self.transform
    
    # return a single list containing all descendants
    def getDescendantList(self):
        """
        Obtiene una lista plana de todos los descendientes de este objeto en el grafo de escena.

        Returns:
            list: Lista que contiene todos los descendientes del objeto.
        """
        # master list of all descendant nodes
        descendants = []
        # nodes to be added to descendant list,
        # and whose children will be added to this list
        nodesToProcess = [self]
        # continue processing nodes while any are left
        while len( nodesToProcess ) > 0:
            # remove first node from list
            node = nodesToProcess.pop(0)
            # add this node to descendant list
            descendants.append(node)
            # children of this node must also be processed 
            nodesToProcess = node.children +nodesToProcess
        return descendants
    


    # apply geometric transformations 
    def applyMatrix(self, matrix, localCoord=True):
        """
        Aplica una matriz de transformación a este objeto.

        Args:
            matrix (numpy.ndarray): La matriz de transformación a aplicar.
            localCoord (bool): Indica si la transformación se aplica en coordenadas locales o globales.

        Returns:
            None
        """ 
        if localCoord: 
            self.transform = self.transform @ matrix 
        else: 
            self.transform = matrix @ self.transform

    def translate(self, x,y,z, localCoord=True): 
        """
        Realiza una traslación del objeto.

        Args:
            x (float): Valor de traslación en el eje X.
            y (float): Valor de traslación en el eje Y.
            z (float): Valor de traslación en el eje Z.
            localCoord (bool): Indica si la traslación se realiza en coordenadas locales o globales.

        Returns:
            None
        """
        m = Matrix.makeTranslation(x,y,z) 
        self.applyMatrix(m, localCoord)

    def rotateX(self, angle, localCoord=True): 
        """
        Realiza una rotación en el eje X.

        Args:
            angle (float): Ángulo de rotación en radianes.
            localCoord (bool): Indica si la rotación se realiza en coordenadas locales o globales.

        Returns:
            None
        """
        m = Matrix.makeRotationX(angle) 
        self.applyMatrix(m, localCoord)

    def rotateY(self, angle, localCoord=True): 
        """
        Realiza una rotación en el eje Y.

        Args:
            angle (float): Ángulo de rotación en radianes.
            localCoord (bool): Indica si la rotación se realiza en coordenadas locales o globales.

        Returns:
            None
        """
        m = Matrix.makeRotationY(angle) 
        self.applyMatrix(m, localCoord)

    def rotateZ(self, angle, localCoord=True): 
        """
        Realiza una rotación en el eje Z.

        Args:
            angle (float): Ángulo de rotación en radianes.
            localCoord (bool): Indica si la rotación se realiza en coordenadas locales o globales.

        Returns:
            None
        """
        m = Matrix.makeRotationZ(angle) 
        self.applyMatrix(m, localCoord)

    def scale(self, s, localCoord=True): 
        """
        Realiza una escala del objeto.

        Args:
            s (float): Factor de escala uniforme.
            localCoord (bool): Indica si la escala se realiza en coordenadas locales o globales.

        Returns:
            None
        """
        m = Matrix.makeScale(s) 
        self.applyMatrix(m, localCoord)

    # get/set position components of transform 
    def getPosition(self):
        """
        Obtiene las componentes de posición de la transformación del objeto.

        Returns:
            list: Lista que contiene las componentes [x, y, z] de la posición.
        """
        return [ self.transform.item((0,3)), 
                 self.transform.item((1,3)), 
                 self.transform.item((2,3)) ]

    def getWorldPosition(self):
        """
        Obtiene la posición del objeto en coordenadas mundiales.

        Returns:
            list: Lista que contiene las componentes [x, y, z] de la posición en coordenadas mundiales.
        """
        worldTransform = self.getWorldMatrix() 
        return [ worldTransform.item((0,3)),
                 worldTransform.item((1,3)),
                 worldTransform.item((2,3)) ]

    def setPosition(self, position): 
        """
        Establece las componentes de posición de la transformación del objeto.

        Args:
            position (list): Lista que contiene las componentes [x, y, z] de la posición.

        Returns:
            None
        """
        self.transform.itemset((0,3), position[0]) 
        self.transform.itemset((1,3), position[1])
        self.transform.itemset((2,3), position[2])