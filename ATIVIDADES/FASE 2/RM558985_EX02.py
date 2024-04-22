
valor_carro = float(input("Informe o valor do carro: "))
print(f"o preço final à vista com o desconto de 20% é de R${valor_carro * 0.8:.2f}")
for parcelas in range (6,61,6):
    if parcelas == 1:
        preco_final = valor_carro * 0.8  
    else:
        acrescimo = {6: 1.05, 12: 1.1, 18: 1.15, 24: 1.2, 30: 1.25, 36: 1.3, 42: 1.35, 48: 1.4, 54: 1.45, 60: 1.5}[parcelas]
        preco_final = valor_carro * acrescimo
    valor_parcela = preco_final / parcelas
    
    print(f"o preço final parcelado em {parcelas} X é de R${preco_final:.2f} com parcelas de R$ {valor_parcela:.2f} \t ")