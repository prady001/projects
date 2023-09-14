from solution import Carrinho


carrinho1 = Carrinho()
carrinho2 = Carrinho()

carrinho1.adiciona('banana', 5)
print(carrinho1.total_do_produto('banana'))  # Vai imprimir 5
print(carrinho2.total_do_produto('banana'))  # Vai imprimir 0

# Adiciona alguns produtos
carrinho1.adiciona('abacate', 7)
carrinho1.adiciona('banana', 4)
carrinho2.adiciona('banana', 3)

print(carrinho1.total_do_produto('abacate'))  # Vai imprimir 7
print(carrinho1.total_do_produto('banana'))  # Vai imprimir 9
print(carrinho2.total_do_produto('abacate'))  # Vai imprimir 0
print(carrinho2.total_do_produto('banana'))  # Vai imprimir 3
