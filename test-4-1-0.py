from core.base import Base 
from core.renderer import Renderer 
from core.scene import Scene 
from core.camera import Camera 
from core.mesh import Mesh 

from geometry.hexagon import HexagonGeometry #importamos la figura hexagono
from material.surfaceMaterial import SurfaceMaterial

# render a basic scene 
class Test(Base):
    def initialize(self): 
        """
        Inicializa la configuración para el programa.

        Returns:
            None
        """
        print("Initializing program...")
        self.renderer = Renderer() 
        self.scene = Scene() 
        self.camera = Camera( aspectRatio=800/600 ) 
        self.camera.setPosition([0, 0, 4])
        geometry = HexagonGeometry()
        material = SurfaceMaterial( {"useVertexColors": True} ) 
        #material = SurfaceMaterial({ "useVertexColors": True, "wireframe": True, "lineWidth": 8 })
        self.mesh = Mesh( geometry, material ) 
        self.scene.add( self.mesh )
        
    def update(self):
        """
        Actualiza el programa en cada fotograma.

        Returns:
            None
        """
        self.mesh.rotateY( 0.0514 )
        self.mesh.rotateX( 0.0337 )
        self.renderer.render( self.scene, self.camera )
    
# Instancia esta clase y ejecuta el programa

Test( screenSize=[800,600] ).run()