"""
Escrito por Alexander DIniz dos Santos para avaliação de perfil.

Este script busca solucionar a seguinte questão:
        QUESTÃO 01
    Dado um array de números inteiros, retorne os índices dos dois números de forma que eles se
    somem a um alvo específico.
    Você pode assumir que cada entrada teria exatamente uma solução, e você não pode usar o
    mesmo elemento duas vezes.
"""

#!/bin/sh

def sum_to_target(num_list, alvo):
    """
    Busca somas (dois números) fornecidos na num_list
    que resultem no valor da variável alvo.

    :type num_list: List[int]
    :type alvo: int
    :rtype: List[int]
    """
    
    # Validação de dados
    if not isinstance(alvo, int):
        raise TypeError("Parâmetro 'alvo' deveria ser um inteiro.")
    if not isinstance(num_list, list):
        raise TypeError("Parâmetro 'num_list' deveria ser uma lista.")
    if not all(isinstance(num, int) for num in num_list):
        raise TypeError("A lista 'num_list' deveria apenas conter inteiros.")

    mapa_valores = {}
    NUM_LIST_LEN = range(len(num_list)) # Tamanho da lista num_list
    for i in NUM_LIST_LEN: # Iterando num_list
        num = num_list[i] # Número que estamos usando para comparação
        par = alvo - num # O número que precisamos achar na lista
        if par in mapa_valores: # Se isto aqui for válido, o par foi encontrado na lista.
            return [mapa_valores[par], i] # Retorna uma lista com o resultado
        mapa_valores[num] = i # Guarda no mapa
    return # Não encontrado.