import requests
import json

def dolar():
    response = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='02-18-2022'&$top=10&$format=json&$select=cotacaoVenda")
    dados = json.loads(response.content)

    return dados["value"][0]['cotacaoVenda']
