"""
Escrito por Alexander DIniz dos Santos para avaliação de perfil.

Este script busca solucionar a seguinte questão:
        QUESTÃO 02
    Um bracket é considerado qualquer um dos seguintes caracteres: (, ), {, }, [ ou ].
Dois brackets são considerados um par combinado se o bracket de abertura (isto é, (, [ou {) ocorre à esquerda 
de um bracket de fechamento (ou seja,),] ou} do mesmo tipo exato. 
Existem três tipos de pares de brackets : [], {} e ().
Um par de brackets correspondente não é balanceado se o de abertura e o de fechamento 
não corresponderem entre si. Por exemplo, {[(])} não é balanceado porque o conteúdo entre {e} não é balanceado. 
O primeiro bracket inclui o de abertura, (, e o segundo inclui um bracket de fechamento desbalanceado,].
Dado sequencias de caracteres, determine se cada sequência de brackets é balanceada. 
Se uma string estiver balanceada, retorne SIM. Caso contrário, retorne NAO.
"""

def is_balanced(word):
    """
    Determina se a string recebida tem brackets balanceados.

    :type word: str
    :rtype str
    """

    brackets_de_abertura = tuple('({[')
    brackets_de_fechamento = tuple(')}]')
    mapa_brackets = dict(zip(brackets_de_abertura, brackets_de_fechamento)) # Mapeando abertura/fechamento
    queue = []

    for char in word:
        if char in brackets_de_abertura:
            queue.append(mapa_brackets[char])
        elif char in brackets_de_fechamento:
            if not queue or char != queue.pop():
                return "NÃO"
    return "SIM" if not queue else "NAO"

print("TESTE " + is_balanced("{[()]}"))
print("TESTE " + is_balanced("{[(])}"))
print("TESTE " + is_balanced("{{[[(())]]}}"))