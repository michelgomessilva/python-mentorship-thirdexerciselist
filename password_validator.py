"""
2. Validação de Entrada (Estrutura: while)
Enunciado: Crie um programa que peça ao usuário para digitar uma senha. 
O programa deve continuar pedindo a senha (repetindo a leitura) enquanto 
o valor digitado for diferente de "python123". Quando a senha correta 
for inserida, exiba a mensagem "Acesso Permitido".

Objetivo: Praticar laços condicionais e validação de fluxo.
-------------------------------------------------------------------------------------------------------
"""

try:
    # 1. Configurações do Sistema
    SECRET_PASSWORD = "python123"
    MAX_ATTEMPTS = 5  # Adicionamos um limite por segurança (Boa prática de Back-end)
    attempts = 0
    access_granted = False

    # 2. Laço de Validação (While)
    # O loop continua enquanto a senha for errada E não estourar as tentativas
    while not access_granted:
        user_input = input("Digite a senha de acesso: ").strip()
        attempts += 1

        # Cláusula de Guarda: Verifica se a senha está correta
        if user_input == SECRET_PASSWORD:
            print("\n Acesso Permitido")
            access_granted = True
        
        else:
            print(f" Senha incorreta. Tentativa {attempts}/{MAX_ATTEMPTS}")
            
            # Verificação de limite de segurança
            if attempts >= MAX_ATTEMPTS:
                print("\n Conta bloqueada por excesso de tentativas.")
                break

except KeyboardInterrupt:
    print("\n\n Operação cancelada pelo usuário. Desconectando...")

except Exception as e:
    print(f"Erro inesperado no sistema: {e}")