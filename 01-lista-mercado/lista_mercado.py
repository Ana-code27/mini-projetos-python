def mostrar_menu():
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Ver lista')
    print('4. Sair')


def pedir_numeros (mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print('Por favor, digite um número positivo.')
            else:
                return valor
        except ValueError:
            print('-------------------------------------')
            print('Entrada inválida. Por favor, digite um número inteiro.')
            print('-------------------------------------')
 
def adicionar_item(compras):
    item = input('Digite um item: ').lower()
    qtd = pedir_numeros('Quantidade: ')
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
            qtd = pedir_numeros('Quantidade a remover: ')
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
        resposta = pedir_numeros('Digite a opção desejada: ')
        
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
            print('-------------------------------------')
            print('Entrada inválida. Por favor, digite uma opção válida')
            print('-------------------------------------')
main()