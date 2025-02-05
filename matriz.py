class Matriz:
    """
    Clase que representa una matriz y proporciona métodos para su manipulación.
    No tiene atributos propios, ya que los vectores se pasan como parámetros en los métodos.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase Matriz.
        Este constructor no recibe parámetros ni realiza ninguna operación específica.
        """
        pass
    
    def crear_matriz(self,v1=[], v2=[], v3=[]):
        """
        Crea una matriz a partir de tres vectores (listas) proporcionados.
        Este método toma tres vectores (listas) como parámetros y los combina en una sola matriz
        de tamaño 3xn, donde 'n' es la longitud de los vectores. Los vectores deben tener la misma
        longitud para formar una matriz válida.
        """
        matriz = [v1, v2, v3]
        return matriz
    