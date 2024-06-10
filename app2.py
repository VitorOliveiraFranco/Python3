import os
from avaliacao import Avaliacao

class Restaurante:
    restaurantes=[]
    
    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._avaliacao=[]
        self._ativo=False
        
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('LISTANDO RESTAURANTES\n')
        for restaurante in cls.restaurantes:
            nome_do_restaurante=restaurante._nome
            categoria=restaurante._categoria
            ativo= 'Ativado' if restaurante._ativo else 'Desativado'
            print(f'- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
        voltar_menu_principal()

    @classmethod
    def procurar_restaurante(cls, nome):
        restaurante_encontrado=False
        for restaurante in cls.restaurantes:
            if nome.title() == restaurante._nome:
                restaurante_encontrado=True
                return restaurante
        if not restaurante_encontrado:
            print(f'O restaurante {nome} não foi encontrado')
    
    @property
    def alterar_estado_do_restaurante(self):
        self._ativo=not self._ativo
        mensagem=f'O restaurante {self._nome} foi ativado com sucesso' if self._ativo else f'O restaurante {self._nome} foi desativado com sucesso'
        print(mensagem)
        voltar_menu_principal()
        
def exibir_nome_do_programa():
    print('Sabor Express')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')
    
def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()
    
def opcao_invalida():
    print('Opção invalida\n')
    voltar_menu_principal()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_do_restaurante=input('Digite o nome do restaurante que você quer cadastrar: ')
    categoria=input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante=Restaurante(nome_do_restaurante, categoria)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

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
            nome_do_restaurante=input('Digite o nome do restaurante que você deseja alterar o estado:')
            acho_nome=Restaurante.procurar_restaurante(nome_do_restaurante)
            acho_nome.alterar_estado_do_restaurante
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