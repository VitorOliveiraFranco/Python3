import os
from restaurante import Restaurante

def exibir_nome_do_programa():
    print('Sabor Express')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Fazer uma avaliação')
    print('5. Sair')
    print()
    
def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()
    
def opcao_invalida():
    print('Opção invalida')
    print()
    voltar_menu_principal()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_do_restaurante=input('Digite o nome do restaurante que você quer cadastrar: ')
    print()
    categoria=input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    print()
    dados_do_restaurante=Restaurante(nome_do_restaurante, categoria)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    print()
    voltar_menu_principal()

def finalizar_app():
    exibir_subtitulo('App finalizado')

def exibir_subtitulo(texto):
    os.system('cls')
    linha='*'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():
    try:
        opcao_escolhida=int(input('Escolha uma opção: '))
        
        if opcao_escolhida==1:  
            cadastrar_novo_restaurante()
        elif opcao_escolhida==2:
            Restaurante.listar_restaurantes()
        elif opcao_escolhida==3:
            exibir_subtitulo('Alterando estado do restaurante')
            nome_do_restaurante=input('Digite o nome do restaurante que você deseja alterar o estado: ')
            achou_nome=Restaurante.procurar_restaurante(nome_do_restaurante)
            achou_nome.alterar_estado_do_restaurante
        elif opcao_escolhida==4:
            exibir_subtitulo('Fazendo uma avaliação')
            nome_do_restaurante=input('Digite o nome do restaurante que você deseja fazer uma avaliação: ')
            print('')
            achou_nome=Restaurante.procurar_restaurante(nome_do_restaurante)
            cliente=input('Digite seu nome: ')
            print('')
            nota=int(input('Digite uma nota: '))
            print('')
            achou_nome.receber_avaliacao(cliente, nota)
        elif opcao_escolhida==5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__=='__main__':
    main()