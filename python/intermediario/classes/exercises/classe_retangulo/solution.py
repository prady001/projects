class Retangulo:
    
    def __init__(self, ponto_inferior_esquerdo, ponto_superior_direito):
        self.ponto_inferior_esquerdo = ponto_inferior_esquerdo
        self.ponto_superior_direito = ponto_superior_direito

    def calcula_perimetro(self):
        largura = abs(self.ponto_superior_direito.x - self.ponto_inferior_esquerdo.x)
        altura = abs(self.ponto_superior_direito.y - self.ponto_inferior_esquerdo.y)
        return 2 * (largura + altura)

    def calcula_area(self):
        largura = abs(self.ponto_superior_direito.x - self.ponto_inferior_esquerdo.x)
        altura = abs(self.ponto_superior_direito.y - self.ponto_inferior_esquerdo.y)
        return largura * altura

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

