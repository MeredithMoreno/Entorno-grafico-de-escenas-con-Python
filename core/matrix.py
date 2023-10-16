import numpy 
from math import sin, cos, tan, pi
class Matrix(object):
    @staticmethod 
    def makeIdentity():
        """
        Devuelve una matriz de identidad 4x4.

        Returns:
            numpy.ndarray: Matriz de identidad.
        """
        return numpy.array( [[1, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]] ).astype(float)
    @staticmethod 
    def makeTranslation(x, y, z):
        """
        Devuelve una matriz de traslación 4x4.

        Args:
            x (float): Valor de traslación en el eje X.
            y (float): Valor de traslación en el eje Y.
            z (float): Valor de traslación en el eje Z.

        Returns:
            numpy.ndarray: Matriz de traslación.
        """
        return numpy.array([[1, 0, 0, x],
                            [0, 1, 0, y],
                            [0, 0, 1, z],
                            [0, 0, 0, 1]]).astype(float)
    @staticmethod 
    def makeRotationX(angle):
        """
        Devuelve una matriz de rotación en el eje X 4x4.

        Args:
            angle (float): Ángulo de rotación en radianes.

        Returns:
            numpy.ndarray: Matriz de rotación en el eje X.
        """
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[1, 0, 0, 0],
                            [0, c, -s, 0],
                            [0, s, c, 0],
                            [0, 0, 0, 1]]).astype(float)
    @staticmethod
    def makeRotationY(angle):
        """
        Devuelve una matriz de rotación en el eje Y 4x4.

        Args:
            angle (float): Ángulo de rotación en radianes.

        Returns:
            numpy.ndarray: Matriz de rotación en el eje Y.
        """
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[ c, 0, s, 0],
                            [ 0, 1, 0, 0],
                            [-s, 0, c, 0],
                            [ 0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makeRotationZ(angle):
        """
        Devuelve una matriz de rotación en el eje Z 4x4.

        Args:
            angle (float): Ángulo de rotación en radianes.

        Returns:
            numpy.ndarray: Matriz de rotación en el eje Z.
        """
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[c, -s, 0, 0],
                            [s, c, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]]).astype(float)
    @staticmethod
    def makeScale(s):
        """
        Devuelve una matriz de escala 4x4.

        Args:
            s (float): Factor de escala uniforme.

        Returns:
            numpy.ndarray: Matriz de escala.
        """
        return numpy.array([[s, 0, 0, 0],
                            [0, s, 0, 0],
                            [0, 0, s, 0],
                            [0, 0, 0, 1]]).astype(float)
    
    @staticmethod
    def makePerspective(angleOfView=60,aspectRatio=1, near=0.1, far=1000):
        """
        Devuelve una matriz de proyección perspectiva 4x4.

        Args:
            angleOfView (float): Ángulo de visión en grados.
            aspectRatio (float): Relación de aspecto.
            near (float): Distancia cercana al plano de visión.
            far (float): Distancia lejana al plano de visión.

        Returns:
            numpy.ndarray: Matriz de proyección perspectiva.
        """
        a = angleOfView * pi/180.0
        d = 1.0 / tan(a/2)
        r = aspectRatio
        b = (far + near) / (near - far)
        c = 2*far*near / (near - far)
        return numpy.array([[d/r, 0, 0, 0],
                            [0, d, 0, 0],
                            [0, 0, b, c],
                            [0, 0, -1, 0]]).astype(float)