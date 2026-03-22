"""
4. Simulação de Caixa Eletrônico
Enunciado: Desenvolva um programa que simule um saque em um caixa eletrônico. 
O usuário deve informar o valor que deseja sacar (inteiro). O programa deve 
utilizar um laço while para calcular o menor número de cédulas possíveis 
para entregar o valor, utilizando notas de R$ 50, R$ 20, R$ 10 e R$ 1.

Dica: A cada iteração, verifique se o valor restante é maior ou igual à nota atual; 
se for, subtraia o valor da nota e conte uma cédula. Quando não for mais possível 
usar a nota atual, passe para a próxima nota menor.

Objetivo: Praticar laços de repetição com redução de montante (Greedy Algorithm).
-------------------------------------------------------------------------------------------------------
"""

try:
    # 1. Entrada de Dados com Validação Inicial
    print("--- CAIXA ELETRONICO ---")
    withdrawal_value = input("Digite o valor que deseja sacar (apenas numeros inteiros): ").strip()

    # Validação: Garante que a entrada seja numérica e positiva
    if not withdrawal_value.isdigit():
        print("Erro: O valor informado deve ser um numero inteiro positivo.")
    else:
        remaining_balance = int(withdrawal_value)
        
        # Guard Clause: Evita processar saques de R$ 0
        if remaining_balance == 0:
            print("Erro: Valor de saque deve ser maior que zero.")
        else:
            # 2. Configuração do Sistema de Cédulas
            current_bill_value = 50
            bills_counter = 0

            print(f"Processando saque de R$ {remaining_balance}...")
            print("-" * 30)

            # 3. Laço Principal de Contagem (Lógica de Decréscimo)
            while True:
                if remaining_balance >= current_bill_value:
                    remaining_balance -= current_bill_value
                    bills_counter += 1
                else:
                    # Se houveram notas contadas da denominação atual, exibe o resultado
                    if bills_counter > 0:
                        print(f"Total de {bills_counter} cedulas de R$ {current_bill_value}")
                    
                    # Lógica de Troca de Cédula (Escada de valores)
                    if current_bill_value == 50:
                        current_bill_value = 20
                    elif current_bill_value == 20:
                        current_bill_value = 10
                    elif current_bill_value == 10:
                        current_bill_value = 1
                    
                    # Reinicia o contador para a próxima nota
                    bills_counter = 0

                    # Condição de Parada: Quando o valor chegar a zero
                    if remaining_balance == 0:
                        break

            print("-" * 30)
            print("Saque finalizado com sucesso.")

except KeyboardInterrupt:
    print("\nOperacao cancelada pelo usuario.")

except Exception as e:
    print(f"Erro inesperado no sistema: {e}")