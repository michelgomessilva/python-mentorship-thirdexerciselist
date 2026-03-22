"""
1. Soma de Intervalo
Escreva um programa que utilize um laço for para calcular a soma de todos os 
números inteiros de 1 a 100 (inclusive). Ao final, exiba o resultado total no console.

Objetivo: Praticar iteração controlada e acumuladores.
-------------------------------------------------------------------------------------------------------
"""

try:
    # 1. Definição de Constantes (Configurável para outros intervalos)
    START = 1
    END = 100
    
    # 2. Inicialização do Acumulador
    total_sum = 0

    # 3. Processamento com Laço de Repetição
    # O range(start, stop) é exclusivo no stop, por isso somamos + 1
    for number in range(START, END + 1):
        total_sum += number

    # 4. Saída de Dados
    print(f"A soma de todos os números de {START} a {END} é: {total_sum}")

    # --- VALIDAÇÃO DE ENGENHARIA (Teste Unitário Mental) ---
    # Existe uma fórmula matemática (Soma de Gauss) para validar o resultado:
    # S = (n * (n + 1)) / 2
    # Para 100: (100 * 101) / 2 = 5050
    
    expected_value = (END * (END + 1)) // 2
    if total_sum == expected_value:
        print("✅ Validação matemática: SUCESSO (Resultado íntegro).")
    else:
        print("❌ Validação matemática: FALHA (Erro de processamento).")

except Exception as e:
    print(f"Erro inesperado no processamento: {e}")