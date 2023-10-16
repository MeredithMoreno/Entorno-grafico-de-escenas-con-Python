from core.object3D import Object3D

class Group(Object3D):
    def __init__(self): 
        """
        Inicializa una instancia de la clase Group, que representa un grupo de objetos en una escena 3D.

        Esta clase actúa como un contenedor para objetos 3D y hereda propiedades y funcionalidades de la clase Object3D.

        Args:
            No se requieren argumentos específicos para la inicialización.
        """
        super().__init__()
