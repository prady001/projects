class Foguete:
    def __init__(self, velocidade_kmph):
        self.velocidade_kmph = velocidade_kmph  # Velocidade do foguete em km/h
        self.distancia_percorrida_km = 0.0  # Inicializa a distância percorrida como 0 km

    def atualizar(self, tempo_segundos):
        # Calcula a distância total percorrida usando a fórmula: distância = velocidade * tempo
        distancia_km = (self.velocidade_kmph * tempo_segundos) / 3600  # Converter horas para segundos
        self.distancia_percorrida_km += distancia_km  # Atualiza a distância percorrida
        return self.distancia_percorrida_km

