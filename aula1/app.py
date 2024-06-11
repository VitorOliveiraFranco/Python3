# print ('Olá mundo, Python!!')
    
import os
    
# restaurantes=['PythonBurguer','Madalousso','Notubo']

# dicionário - relação chave e valor
restaurantes = [{'nome':'Pão com Banha','categoria':'gourmet', 'ativo':False},
                {'nome':'Saco do Feijão','categoria':'feijoada', 'ativo':True},
                {'nome':'Bife Sujo','categoria':'churrascaria', 'ativo':False}]
    
def exibir_nome_do_programa():
    print('𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼')
        
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')
    
def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()
    
def opcao_invalida():
    print('Opção inválida\n')
    voltar_menu_principal()
    
def cadastrar_novo_restaurante():
    
    ''' 
    
        Essa função é responsável por cadastrar novo restaurante
    
            Inputs:
                - Nome do restaurante
                - Categoria
        
            Outputs:  
                - Adiciona um novo restaurante ao dicionário restaurantes
        
    '''
    
    exibir_subtitulo('CADASTRO DE NOVOS RESTAURANTES')
    nome_do_restaurante=input('Digite o nome do restaurante que você quer cadastrar: ')
    categoria =input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    # criar formato do dicionário pra daí apendar
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('LISTANDO RESTAURANTES\n')
    
    for restaurante in restaurantes:
        # print(restaurante)
        nome_do_restaurante=restaurante['nome']
        categoria = restaurante['categoria']
        ativo= 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
    voltar_menu_principal()

def alterar_estado_do_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_do_restaurante=input('Digite o nome do restaurante que você deseja alterar o estado: ')
    restaurante_encontrado=False
    
    for restaurante in restaurantes:
        if nome_do_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)
        
    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado')
    
    voltar_menu_principal()

def finalizar_app():
    exibir_subtitulo('Finalizar app')
        
def exibir_subtitulo(texto):
    os.system('cls')
    linha='*'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def escolher_opcao():
    try:
        opcao_escolhida=int(input("Escolha uma opção: "))
        
        if opcao_escolhida==1:
            # print('Você escolheu cadastrar um restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida==2:
            # print('Você escolheu listar os restaurantes')
            listar_restaurantes()
        elif opcao_escolhida==3:
            # print('ativar restaurante')
            alterar_estado_do_restaurante()
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
    
    
        
        