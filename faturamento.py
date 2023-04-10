import json

with open('faturamento.json', 'r') as faturamento:
    dados = json.load(faturamento)

faturamento_diario = dados['faturamento_diario']

maior = max(faturamento_diario)
menor = min([faturamento for faturamento in faturamento_diario if faturamento > 0]) #Caso queira o faturamento do final de semana -->: menor = min(faturamento_diario) seria igual a 0.0#

dias_uteis = len([faturamento for faturamento in faturamento_diario if faturamento > 0])
media = sum(faturamento_diario) / dias_uteis

dias_acima_da_media = len([faturamento for faturamento in faturamento_diario if faturamento > media])

print('Maior valor de faturamento:', maior)
print('Menor valor de faturamento:', menor)
print('Numero de dias com faturamento acima da média mensal:', dias_acima_da_media)