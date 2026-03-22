"""
1. Sistema de Gestão de Inventário Premium
Enunciado: Gerenciar o estoque de uma loja de eletrônicos usando Dicionários, 
Sets, Tuplas e Listas. O sistema deve permitir adicionar produtos, extrair 
categorias únicas, gerar relatórios de baixo estoque e calcular o valor total.

Objetivo: Aplicar SOLID, funções modulares e estruturas de dados compostas.
-------------------------------------------------------------------------------------------------------
"""

import sys
from typing import Dict, List, Set, Tuple, Any, Union

# --- FUNÇÕES DE LÓGICA (CORE BUSINESS EM INGLÊS) ---

def add_product(
    inventory: Dict[str, Any], 
    prod_id: str, 
    name: str, 
    price: float, 
    quantity: int, 
    categories: Union[List[str], str]
) -> bool:
    """Adiciona ou atualiza um produto no dicionário de estoque."""
    
    # Normalização: garante que categorias seja sempre uma lista
    if not isinstance(categories, list):
        categories = [categories]
        
    inventory[prod_id] = {
        "name": name.strip().title(),
        "price": float(price),
        "quantity": int(quantity),
        "categories": [cat.strip().lower() for cat in categories]
    }
    return True


def get_unique_categories(inventory: Dict[str, Any]) -> Set[str]:
    """Retorna um Set com todas as categorias distintas do estoque."""
    all_categories: Set[str] = set()
    for product in inventory.values():
        # Operação de união de Sets para performance
        all_categories.update(product["categories"])
    return all_categories


def get_low_stock_report(inventory: Dict[str, Any], limit: int = 5) -> List[Tuple[str, int]]:
    """Retorna lista de tuplas (nome, quantidade) para itens abaixo do limite."""
    # List Comprehension para filtragem elegante
    return [
        (product["name"], product["quantity"]) 
        for product in inventory.values() 
        if product["quantity"] < limit
    ]


def calculate_total_inventory_value(inventory: Dict[str, Any]) -> float:
    """Calcula o valor financeiro total (Preço * Quantidade)."""
    total_value: float = 0.0
    for product in inventory.values():
        total_value += product["price"] * product["quantity"]
    return total_value


# --- INTERFACE DE USUÁRIO (MENU EM PORTUGUÊS) ---

def display_menu() -> str:
    """Exibe o menu do sistema e retorna a opção escolhida."""
    print("\n--- SISTEMA DE GESTAO DE INVENTARIO ---")
    print("1. Adicionar Produto")
    print("2. Listar Categorias Unicas")
    print("3. Relatorio de Baixo Estoque")
    print("4. Valor Total do Patrimonio")
    print("5. Sair")
    return input("Selecione uma opcao: ").strip()


def main() -> None:
    # Nosso "Banco de Dados" em memória
    central_inventory: Dict[str, Any] = {}

    while True:
        option = display_menu()

        try:
            if option == "1":
                pid = input("ID do Produto: ").strip()
                name = input("Nome: ").strip()
                price = input("Preco: ").strip()
                qty = input("Quantidade: ").strip()
                cats = input("Categorias (separadas por virgula): ").split(",")
                
                add_product(central_inventory, pid, name, float(price), int(qty), cats)
                print("Produto registrado com sucesso.")

            elif option == "2":
                unique_cats = get_unique_categories(central_inventory)
                print(f"Categorias disponiveis: {', '.join(unique_cats) if unique_cats else 'Nenhuma'}")

            elif option == "3":
                low_stock_list = get_low_stock_report(central_inventory)
                if not low_stock_list:
                    print("Todo o estoque esta em niveis seguros.")
                else:
                    print("Produtos com baixo estoque (menos de 5 unidades):")
                    for product_name, quantity in low_stock_list:
                        print(f"- {product_name}: {quantity} unidades")

            elif option == "4":
                total = calculate_total_inventory_value(central_inventory)
                print(f"Valor total investido em estoque: R$ {total:.2f}")

            elif option == "5":
                print("Encerrando sistema...")
                break
            
            else:
                print("Opcao invalida. Tente novamente.")

        except ValueError:
            print("Erro: Preco e Quantidade devem ser valores numericos.")
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSistema interrompido pelo administrador.")
        sys.exit()