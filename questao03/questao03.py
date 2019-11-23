"""
Escrito por Alexander DIniz dos Santos para avaliação de perfil.

Este script busca solucionar a seguinte questão:
        QUESTÃO 03
    Digamos que você tenha um array para o qual o elemento i é o preço de uma 
determinada ação no dia i. Se você tivesse permissão para concluir no máximo uma 
transação (ou seja, comprar uma e vender uma ação), crie um algoritmo para encontrar
o lucro máximo. 
    Note que você não pode vender uma ação antes de comprar
"""

def find_max_profit(arr):
    """ 
    Busca o dia que fornece maior ROI para compra/venda de ações dadas em um array. 

    :type arr: List[int]
    :rtype int
    """
    if not isinstance(arr, list):
        raise TypeError("Parâmetro 'arr' deve ser do tipo list.")
    if not all(isinstance(elem, int) for elem in arr):
        raise TypeError("Um dos elementos do parâmetro 'arr' não é do tipo int.")

    min = None
    max = None
    dia_compra = None
    dia_venda = None # Poderia usar 0, mas no caso de retorno 0 daria erro

    for index, elem in enumerate(arr):
        # A próxima linha poderia ser feita com a função min()
        # Mas estou em busca de algoritmo ótimo
        # Usar min() acrescentaria N em complexidade do algoritmo,
        if min is None or elem < min: # is None para o ciclo inicial
            min = elem
            dia_compra = index
        
        # Compra com maior ROI
        elif (max is None) or (elem - min) > max:
            max = elem - min
            dia_venda = index

    return dia_venda + 1 if dia_venda else 0 # Index inicia de 0, a contagem de dias de 1