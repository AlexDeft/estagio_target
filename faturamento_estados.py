faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento_estados.values())

porcentagem = {}
for estado, valor in faturamento_estados.items():
    porcentagem[estado] = (valor / total) * 100

for estado, porcentagem in porcentagem.items():
    print(f'{estado} : {porcentagem:.2f}%')
