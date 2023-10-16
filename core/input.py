import pygame

class Input(object):
    def __init__(self):
        """
        Inicializa una instancia de la clase Input, que se encarga de gestionar la entrada del usuario.

        Esta clase almacena el estado de las teclas del teclado y proporciona métodos para comprobar su estado.

        Args:
            No se requieren argumentos específicos para la inicialización.
        """
        self.quit = False  # Indica si el usuario desea salir de la aplicación

        # Listas para almacenar el estado de las teclas
        # down, up: eventos discretos; duran una sola iteración
        # pressed: evento continuo, entre eventos down y up
        self.keyDownList = []
        self.keyPressedList = []
        self.keyUpList = []

    def update(self):
        """
        Actualiza el estado de las teclas y eventos de entrada del usuario.
        """
        # Restablecer estados de teclas discretas
        self.keyDownList = []
        self.keyUpList = []

        for event in pygame.event.get():
            # Comprobar si se ha solicitado salir de la aplicación al hacer clic en el botón de cerrar ventana
            if event.type == pygame.QUIT:
                self.quit = True

            # Comprobar eventos de pulsación y liberación de teclas;
            # obtener el nombre de la tecla del evento y agregarla o eliminarla de las listas correspondientes
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                self.keyDownList.append(keyName)
                self.keyPressedList.append(keyName)

            if event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                self.keyPressedList.remove(keyName)
                self.keyUpList.append(keyName)

        # Restablecer estados de teclas discretas
        self.keyDownList = []
        self.keyUpList = []

    # Funciones para comprobar el estado de las teclas
    def isKeyDown(self, keyCode):
        """
        Comprueba si una tecla está siendo presionada (discreto).
        
        Args:
            keyCode (str): El nombre de la tecla que se quiere comprobar.

        Returns:
            bool: True si la tecla está siendo presionada, False en caso contrario.
        """
        return keyCode in self.keyDownList

    def isKeyPressed(self, keyCode):
        """
        Comprueba si una tecla está siendo presionada (continuo).

        Args:
            keyCode (str): El nombre de la tecla que se quiere comprobar.

        Returns:
            bool: True si la tecla está siendo presionada, False en caso contrario.
        """
        return keyCode in self.keyPressedList

    def isKeyUp(self, keyCode):
        """
        Comprueba si una tecla está siendo liberada (discreto).

        Args:
            keyCode (str): El nombre de la tecla que se quiere comprobar.

        Returns:
            bool: True si la tecla está siendo liberada, False en caso contrario.
        """
        return keyCode in self.keyUpList
