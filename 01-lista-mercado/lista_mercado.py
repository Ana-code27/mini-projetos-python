def mostrar_menu():
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Ver lista')
    print('4. Sair')

def adicionar_item(compras):
    item = input('Digite um item: ').lower()
    qtd = int(input('Quantidade: '))
    if item in compras:
        compras[item] += qtd
    else:
        compras[item] = qtd
    print('-------------------------------------')
    print(f'Produto {item} adicionado com sucesso!')
    print('-------------------------------------')

def remover_item(compras):
    if not compras:
        print('-------------------------------------')
        print('Sua lista está vazia, nada para remover.')
        print('-------------------------------------')
    else:
        remove_item = input('Digite o item que deseja remover: ').lower()
        if remove_item in compras:
            qtd = int(input('Quantidade a remover: '))
            if qtd >= compras[remove_item]:
                del compras[remove_item]
                print(f'Produto {remove_item} removido totalmente!')
            else:
                compras[remove_item] -= qtd
                print(f'{qtd} unidade(s) de {remove_item} removida(s).')
        else:
            print(f'O item {remove_item} não está na lista.')

def ver_lista(compras):
    print('-------------------------------------')
    print('Confira sua lista de produtos!')
    if not compras:
        print('Sem produtos adicionados.')
    else:
        for item, qtd in compras.items():
            print(f'{item}: {qtd}')
    print('-------------------------------------')

# Programa principal
def main():
    compras = {}
    while True:
        mostrar_menu()
        resposta = int(input('Digite uma opção: '))
        
        if resposta == 1:
            adicionar_item(compras)
        elif resposta == 2:
            remover_item(compras)
        elif resposta == 3:
            ver_lista(compras)
        elif resposta == 4:
            print('-------------------------------------')
            print('Até a próxima!')
            print('-------------------------------------')
            break
        else:
            print('--- OPÇÃO INVÁLIDA. TENTE NOVAMENTE!! ---')
main()