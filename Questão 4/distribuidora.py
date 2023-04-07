info = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}

valorTotal = sum(info.values())

for i in info:
    porcentagem =  (info[i]*100) / valorTotal
    print(f'{i} representa {porcentagem:.2f}% do valor total mensal da distribuidora')