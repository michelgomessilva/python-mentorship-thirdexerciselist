"""
2. Processador de Log de Acessos (Analista de Dados)

Conceitos: Tuplas, Dicionários, Manipulação de Strings, Loops e Funções.

Enunciado: Você recebeu uma lista de tuplas representando logs de um servidor. 
Cada tupla contém (usuario, pagina_acessada, timestamp). Seu objetivo é 
processar esses dados para entender o comportamento dos usuários.

Requisitos:
1. Crie uma função contar_acessos_por_usuario(logs) que retorne um dicionário 
   onde a chave é o nome do usuário e o valor é a quantidade total de páginas 
   que ele acessou.
2. Crie uma função paginas_unicas_visitadas(logs, usuario) que receba o nome 
   de um usuário e retorne um Set com todas as páginas diferentes que ele 
   visitou (removendo duplicatas).
3. Crie uma função que identifique o "Usuário Mais Ativo": ela deve percorrer 
   o dicionário gerado no passo 1 e retornar uma tupla com (nome, total_acessos) 
   do usuário que teve mais entradas no log.
4. Crie um main.py que chama as funções todas como se fosse um menu de sistema 
   e somente pode sair do programa quando o usuário selecionar a opção Sair.
-------------------------------------------------------------------------------------------------------
"""

import sys
from typing import List, Tuple, Dict, Set, Optional

# --- FUNÇÕES DE PROCESSAMENTO (LÓGICA) ---

def count_accesses_by_user(logs: List[Tuple[str, str, str]]) -> Dict[str, int]:
    """
    Calcula o total de acessos para cada usuário presente nos logs.
    """
    access_count: Dict[str, int] = {}
    for entry in logs:
        # Desempacotamento de tupla para clareza: (user, page, timestamp)
        user: str = entry[0]
        access_count[user] = access_count.get(user, 0) + 1
    return access_count


def get_unique_pages_visited(logs: List[Tuple[str, str, str]], target_user: str) -> Set[str]:
    """
    Retorna um conjunto (Set) de páginas únicas acessadas por um usuário específico.
    """
    # Normalização de entrada para busca resiliente
    clean_target: str = target_user.strip().lower()
    
    # Set Comprehension: filtra por usuário e extrai a página (index 1)
    unique_pages: Set[str] = {
        entry[1] for entry in logs 
        if entry[0].lower() == clean_target
    }
    return unique_pages


def identify_most_active_user(access_stats: Dict[str, int]) -> Optional[Tuple[str, int]]:
    """
    Analisa as estatísticas e retorna o usuário com maior número de interações.
    """
    if not access_stats:
        return None

    # max() com key=dict.get é a forma mais performática de encontrar a chave do maior valor
    most_active_name: str = max(access_stats, key=access_stats.get)
    return (most_active_name, access_stats[most_active_name])


# --- INTERFACE E FLUXO PRINCIPAL ---

def display_menu() -> str:
    """Exibe o menu de opções do sistema."""
    print("\n--- SISTEMA DE ANALISE DE LOGS ---")
    print("1. Listar total de acessos por usuario")
    print("2. Listar paginas unicas visitadas por usuario")
    print("3. Exibir usuario mais ativo")
    print("4. Sair")
    return input("Escolha uma opcao: ").strip()


def main() -> None:
    # Base de dados simulada (Lista de Tuplas)
    log_database: List[Tuple[str, str, str]] = [
        ("ana", "home", "09:00"),
        ("bruno", "login", "09:05"),
        ("ana", "config", "09:10"),
        ("carla", "home", "09:15"),
        ("ana", "home", "09:20"),
        ("bruno", "home", "09:25"),
        ("carla", "dashboard", "09:30"),
        ("bruno", "home", "09:35"),
        ("ana", "config", "09:40")
    ]

    while True:
        choice: str = display_menu()

        try:
            if choice == "1":
                stats = count_accesses_by_user(log_database)
                print("\nRelatorio de Acessos:")
                for user, total in stats.items():
                    print(f"Usuario: {user.title()} | Total: {total}")

            elif choice == "2":
                user_name: str = input("Informe o nome do usuario para busca: ")
                unique_pages = get_unique_pages_visited(log_database, user_name)
                
                if unique_pages:
                    print(f"\nPaginas acessadas por {user_name.title()}:")
                    print(", ".join(unique_pages))
                else:
                    print(f"\nNenhum registro encontrado para o usuario '{user_name}'.")

            elif choice == "3":
                stats = count_accesses_by_user(log_database)
                leader = identify_most_active_user(stats)
                
                if leader:
                    name, total = leader
                    print(f"\nUsuario mais ativo: {name.title()}")
                    print(f"Total de acessos registrados: {total}")
                else:
                    print("\nNao ha dados para processar.")

            elif choice == "4":
                print("Encerrando o processador de logs...")
                break
            
            else:
                print("Opcao invalida. Tente novamente.")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSessao finalizada pelo administrador.")
        sys.exit()