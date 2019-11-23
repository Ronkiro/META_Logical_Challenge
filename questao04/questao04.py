"""
Escrito por Alexander DIniz dos Santos para avaliação de perfil.

Este script busca solucionar a seguinte questão:
        QUESTÃO 03
    Dados n inteiros não negativos representando um mapa de elevação onde a largura de cada barra é 1, 
calcule quanta água é capaz de reter após a chuva. 

    [imagem]
"""


def calculate_rain(arr):
    """
    Calcula a quantidade de chuva possível à ser retida.

    :type arr: List[int]
    :rtype int
    """
    
    def left_max(arr):
        """
        Calcula o maior número na sequência pela esquerda e retorna index,
        Ex: [0,1,0,2,1,0,1,3,2,1,2,1] -> 1

        :type arr: Iterable[int]
        :rtype int
        """
        index_max_value = None
        max_value = None

        for index, value in enumerate(arr):
            if max_value is None or value >= max_value:
                max_value = value
                index_max_value = index
            else:
                return index_max_value
        return 0

    def find_water_block(arr):
        """
        Retorna o index do primeiro número maior que o primeiro index
        Ex: [0,1,0,2,1,0,1,3,2,1,2,1] -> 1

        :type arr: Iterable[int]
        :rtype int
        """

        first = arr[0]
        if len(arr) > 1:
            for index, elem in enumerate([-1] + arr[1:]):
                if elem >= first:
                    return index
        return 0

    def find_water(arr, last_block_index=None):
        """
        Calcula a diferença entre os mínimos de uma lista e o menor valor entre
        dois extremos.
        Ex: [2,1,0,1,3] -> 2-1 + 2-0 + 2-1 = 4

        :type arr: List[int]
        :rtype int
        """
        water = 0
        if last_block_index:
            last = last_block_index
            min_extreme = min([arr[0], last]) # Mínimo entre os extremos
        else:
            last=len(arr)
            min_extreme = min([arr[0], arr[last-1]])

        new_arr = arr[1:last-1] # Excluindo os extremos
        for elem in new_arr:
            water += min_extreme - elem # A diferença é o valor da água
        return water

    if not isinstance(arr, list):
        raise TypeError("Parâmetro 'arr' deveria ser do tipo list.")
    if not all((isinstance(elem, int) and elem >= 0) for elem in arr): # Elementos >= 0 e int
        raise TypeError("Elementos de 'arr' devem ser inteiros não negativos.")

    agua = 0

    # Descobrindo o index da maior elevação até encontrar possíveis aguas
    index_max_esquerda = left_max(arr)
    
    # Iterando array invertido para o mesmo caso acima
    index_max_direita = len(arr) - left_max(arr[::-1])

    # Cortando índices desnecessários
    arr = arr[index_max_esquerda:index_max_direita]
    if len(arr) < 3:
        return 0 # Impossível reter água com menos de 3 blocos.
    
    while(1): 
        water_block_end = find_water_block(arr)
        last_block_index = water_block_end + 1 if water_block_end else None
        arr_block = arr[0:last_block_index] # Primeiro bloco possível de se obter agua
        agua += find_water(arr_block, last_block_index)
        arr = arr[water_block_end:]
        if not(water_block_end):
            break
    return agua if agua > 0 else 0