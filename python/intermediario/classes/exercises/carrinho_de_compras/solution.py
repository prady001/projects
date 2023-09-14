class Carrinho:
    def __init__(self):
        self.produtos = {}  # Inicializa um dicionário vazio para armazenar os produtos e seus preços.

    def adiciona(self, nome_produto, preco):
        if nome_produto in self.produtos:
            # Se o produto já existe no carrinho, atualiza o preço somando o novo preço ao valor existente.
            self.produtos[nome_produto] += preco
        else:
            # Se o produto não existe no carrinho, cria uma nova entrada no dicionário.
            self.produtos[nome_produto] = preco

    def total_do_produto(self, nome_produto):
        if nome_produto in self.produtos:
            # Verifica se o produto existe no carrinho e retorna seu preço total.
            return self.produtos[nome_produto]
        else:
            # Se o produto não estiver no carrinho, retorna 0 (ou pode retornar None, dependendo da preferência).
            return 0
