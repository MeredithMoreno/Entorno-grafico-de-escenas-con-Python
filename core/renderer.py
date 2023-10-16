from OpenGL.GL import * 
from core.mesh import Mesh

class Renderer(object):
    def __init__(self, clearColor=[0,0,0]):
        """
        Inicializa un objeto Renderer para la representación gráfica de una escena.

        Args:
            clearColor (list): Color de fondo para limpiar el búfer de color (por defecto, negro).

        Returns:
            None
        """
        glEnable( GL_DEPTH_TEST )

        # Habilita el antialiasing
        glEnable( GL_MULTISAMPLE )
        glClearColor(clearColor[0], clearColor[1],clearColor[2], 1)

    def render(self, scene, camera):
        """
        Realiza la representación gráfica de una escena desde la perspectiva de una cámara.

        Args:
            scene (Scene): La escena que se va a representar.
            camera (Camera): La cámara desde la que se verá la escena.

        Returns:
            None
        """
        # Limpia los búferes de color y profundidad
        glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)

        # Actualiza la vista de la cámara (calcula la matriz inversa)
        camera.updateViewMatrix()

        # extract list of all Mesh objects in scene
        descendantList = scene.getDescendantList()
        meshFilter = lambda x : isinstance(x, Mesh)
        meshList = list( filter( meshFilter,  descendantList ) )
        for mesh in meshList:
            # if this object is not visible,
            # continue to next object in list
            if not mesh.visible:
                continue
            glUseProgram( mesh.material.programRef )
  
            # bind VAO
            glBindVertexArray( mesh.vaoRef )
            
            # update uniform values stored outside of material
            mesh.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data =camera.viewMatrix
            mesh.material.uniforms["projectionMatrix"].data =camera.projectionMatrix

            # update uniforms stored in material
            for variableName, uniformObject in mesh.material.uniforms.items():
                uniformObject.uploadData()

            # update render settings
            mesh.material.updateRenderSettings()

            glDrawArrays( mesh.material.settings["drawStyle"], 0,mesh.geometry.vertexCount )