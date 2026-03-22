"""
3. Filtragem de Dados em Matriz
Enunciado: Dada uma lista de listas (uma matriz) contendo números inteiros, 
utilize laços for aninhados para percorrer todos os elementos. O programa 
deve criar uma nova lista contendo apenas os números que são múltiplos 
de 3 e maiores que 10.

Exemplo de entrada: [[5, 12, 18], [7, 9, 21], [30, 4, 2]]
Saída esperada: [12, 18, 21, 30]

Objetivo: Praticar loops aninhados e condicionais compostas.
-------------------------------------------------------------------------------------------------------
"""

try:
    # 1. Definição da Matriz (Input de dados)
    # Simulamos uma matriz que poderia vir de um sensor ou arquivo JSON
    matrix = [
        [5, 12, 18],
        [7, 9, 21],
        [30, 4, 2]
    ]

    # 2. Inicialização da lista de resultados (Acumulador)
    filtered_numbers = []

    # 3. Processamento com Laços Aninhados
    # O primeiro loop percorre as linhas da matriz (cada sublista)
    for row in matrix:
        # Cláusula de Guarda: Verifica se a linha é realmente uma lista
        if not isinstance(row, list):
            continue

        # O segundo loop percorre cada elemento dentro da linha atual
        for item in row:
            # Validação de tipo: garante que estamos lidando com números
            if not isinstance(item, (int, float)):
                continue

            # Regras de Negócio: Múltiplo de 3 (item % 3 == 0) E Maior que 10
            if item > 10 and item % 3 == 0:
                filtered_numbers.append(item)

    # 4. Saída de Dados
    print("Matriz Original:", matrix)
    print("Numeros Filtrados (Multiplos de 3 e > 10):", filtered_numbers)

except Exception as e:
    print(f"Erro no processamento da matriz: {e}")