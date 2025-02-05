class Componente:
    """
    Clase que proporciona funcionalidades para operaciones relacionadas con matrices.
    No tiene atributos propios, ya que los métodos reciben los datos necesarios como parámetros.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase Componente.
        Este constructor no recibe parámetros ni realiza ninguna operación específica.
        """
        pass
    def transpuesta(self,matriz): 
        """
        Calcula la transpuesta de una matriz dada.
        
        Este método toma una matriz (lista de listas) como entrada y devuelve su transpuesta.
        La transpuesta de una matriz se obtiene intercambiando filas por columnas. Es decir,
        el elemento en la posición (i, j) de la matriz original se coloca en la posición (j, i)
        de la matriz transpuesta.
        """
        filas = len(matriz)
        columnas = len(matriz[0]) if filas > 0 else 0
        matriz_transpuesta = [[0 for i in range(filas)] for i in range(columnas)]

        for i in range(filas):
            for j in range(columnas):
                matriz_transpuesta[j][i] = matriz[i][j]
        return matriz_transpuesta
