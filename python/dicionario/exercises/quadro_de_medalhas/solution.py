def pais_campeao(quadro_de_medalhas):
    pais_campeao = None
    max_medalhas_de_ouro = 0

    for pais, medalhas in quadro_de_medalhas.items():
        if medalhas.get("ouro", 0) > max_medalhas_de_ouro:
            pais_campeao = pais
            max_medalhas_de_ouro = medalhas.get("ouro", 0)
        elif medalhas.get("ouro", 0) == max_medalhas_de_ouro:
            # Em caso de empate de medalhas de ouro, verificamos as medalhas de prata
            if medalhas.get("prata", 0) > quadro_de_medalhas.get(pais_campeao, {}).get("prata", 0):
                pais_campeao = pais
            elif medalhas.get("prata", 0) == quadro_de_medalhas.get(pais_campeao, {}).get("prata", 0):
                # Em caso de empate de medalhas de prata, verificamos as medalhas de bronze
                if medalhas.get("bronze", 0) > quadro_de_medalhas.get(pais_campeao, {}).get("bronze", 0):
                    pais_campeao = pais

    return pais_campeao
