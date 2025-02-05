from model.matriz import Matriz
from components.component_m import Componente

class Servicios:
    """
    Clase que proporciona servicios para operaciones avanzadas con matrices.
    Esta clase utiliza las funcionalidades de las clases `Matriz` y `Componente`
    para realizar operaciones como la creación de matrices y el cálculo de su transpuesta.
    No tiene atributos propios, ya que los métodos reciben los datos necesarios como parámetros.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase Componente.
        Este constructor no recibe parámetros ni realiza ninguna operación específica.
        """
        pass
    def calcular_transpuesta(self, v1=[], v2=[], v3=[]):
        """
        Calcula la transpuesta de una matriz creada a partir de tres vectores.
        Este método utiliza la clase `Matriz` para crear una matriz a partir de tres vectores
        (listas) y luego utiliza la clase `Componente` para calcular la transpuesta de dicha matriz.
        Retorna la matriz transpuesta de tamaño n x 3, donde 'n' es la longitud de los vectores.
        """
        matrz = Matriz()
        m_const = matrz.crear_matriz(v1, v2, v3)
        mtrans = Componente()
        transpuesta = mtrans.transpuesta(m_const)
        return transpuesta

