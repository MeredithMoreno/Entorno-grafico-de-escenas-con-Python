from core.object3D import Object3D 
from core.matrix import Matrix 
from numpy.linalg import inv

class Camera(Object3D):
    def __init__(self, angleOfView=60, aspectRatio=1, near=0.1, far=1000): 
        """
        Inicializa una instancia de la clase Camera.

        Args:
            angleOfView (float): El ángulo de visión de la cámara en grados.
            aspectRatio (float): La relación de aspecto de la cámara.
            near (float): La distancia más cercana desde la cámara a la escena.
            far (float): La distancia más lejana desde la cámara a la escena.
        """
        super().__init__() 
        self.projectionMatrix = Matrix.makePerspective(angleOfView, aspectRatio, near, far)
        self.viewMatrix = Matrix.makeIdentity()

    def updateViewMatrix(self): 
        """
        Actualiza la matriz de vista de la cámara utilizando la matriz del mundo inversa.
        """
        self.viewMatrix = inv( self.getWorldMatrix() )
