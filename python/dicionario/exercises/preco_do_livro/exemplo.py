from solution import verifica_preco


resposta = verifica_preco('Dom Quixote', 
    {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}, 
    {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
)
print(resposta)  # Deve imprimir 40.0

resposta = verifica_preco('Pinóquio', 
    {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}, 
    {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
)
print(resposta)  # Deve imprimir 20.0
