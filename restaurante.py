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
        from app2 import exibir_subtitulo
        exibir_subtitulo('LISTANDO RESTAURANTES')
        
        for restaurante in cls.restaurantes:
            nome_do_restaurante=restaurante._nome
            categoria=restaurante._categoria
            ativo= restaurante.ativo
            print(f'- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {ativo}')
            print()
        from app2 import voltar_menu_principal
        voltar_menu_principal()

    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    @classmethod
    def procurar_restaurante(cls, nome):
        restaurante_encontrado=False
        nome=nome.title()
        for restaurante in cls.restaurantes:
            if nome == restaurante._nome:
                restaurante_encontrado=True
                return restaurante
            
        if not restaurante_encontrado:
            print(f'O restaurante {nome} não foi encontrado')
    
    @property
    def alterar_estado_do_restaurante(self):
        self._ativo=not self._ativo
        mensagem=f'O restaurante {self._nome} foi ativado com sucesso' if self._ativo else f'O restaurante {self._nome} foi desativado com sucesso'
        print()
        print(mensagem)
        print()
        from app2 import voltar_menu_principal
        voltar_menu_principal()
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao=Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        from app2 import voltar_menu_principal
        voltar_menu_principal()

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        
        # soma_das_notas=0
        # for avaliacao in self._avaliacao:   
        #     soma_das_notas+=avaliacao._nota
        # quantidade_de_notas=len(self._avaliacao)
        # media=round(soma_das_notas/quantidade_de_notas)
        # return media
    
        soma_das_notas=sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas=len(self._avaliacao)
        media=round(soma_das_notas/quantidade_de_notas, 1)
        return media