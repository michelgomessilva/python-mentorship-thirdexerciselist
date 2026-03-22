import os
import sys
import subprocess

# Cores ANSI para o terminal
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
MAGENTA = "\033[95m"

def clear_screen():
    """
        Funcao para limpar o ecrã
    """
    # Limpa o ecrã
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Caminho do interpretador python atual para garantir que funciona em qualquer PC
    python_cmd = sys.executable

    while True:
        clear_screen()
        print(f"{YELLOW}{'='*50}{RESET}")
        print(f"{BOLD}{CYAN}{' MAIN HUB - ThirdExerciseList ' : ^50}{RESET}")
        print(f"{BOLD}{CYAN}{' Menu de Exercícios ' : ^50}{RESET}")
        print(f"{YELLOW}{'='*50}{RESET}")
        
        # Lista de opções coloridas baseadas nos ficheiros reais
        print(f"{GREEN}1. {RESET}Soma de Intervalo (1-100)")
        print(f"{GREEN}2. {RESET}Validador de Senha (python123)")
        print(f"{GREEN}3. {RESET}Mineração de Dados em Matriz")
        print(f"{GREEN}4. {RESET}Simulador de Caixa Eletrônico")
        print(f"{GREEN}5. {RESET}Processador de Logs de Servidor")
        print(f"{GREEN}6. {RESET}Gestor de Inventário Premium")
        
        print(f"{YELLOW}{'-' * 50}{RESET}")
        print(f"{RED}{BOLD}0. SAIR{RESET}")
        print(f"{YELLOW}{'-' * 50}{RESET}")

        choice = input(f"{BOLD}Escolha uma opção para executar: {RESET}").strip()

        # Dicionário que mapeia a escolha ao nome do ficheiro real na tua pasta
        scripts = {
            "1": "sum_interval.py",
            "2": "password_validator.py",
            "3": "data_miner.py",
            "4": "atm_simulator.py",
            "5": "server_log_processor.py",
            "6": "inventory_pro_manager.py"
        }

        if choice == "0":
            print(f"\n{BOLD}{GREEN}A encerrar o programa... Até à próxima!{RESET}")
            break
        
        elif choice in scripts:
            script_path = scripts[choice]
            print(f"\n{MAGENTA}--- A EXECUTAR: {script_path} ---{RESET}\n")
            
            # Executa o ficheiro como um processo separado usando subprocess para evitar erros com espaços nos caminhos
            try:
                subprocess.run([python_cmd, script_path], check=True)
            except subprocess.CalledProcessError:
                print(f"\n{RED}Ocorreu um erro ao executar o script.{RESET}")
            except Exception as e:
                print(f"\n{RED}Erro inesperado: {e}{RESET}")

            print(f"\n{YELLOW}{'-'*50}{RESET}")
            input(f"\n{BOLD}Exercício terminado. Pressione ENTER para voltar ao menu...{RESET}")
        
        else:
            print(f"\n{RED}Opção inválida! Tente novamente.{RESET}")
            input(f"\n{BOLD}Pressione ENTER...{RESET}")

if __name__ == "__main__":
    main()
