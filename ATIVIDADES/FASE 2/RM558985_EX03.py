divida=0

while divida <=0:
    divida = float(input('Digite o valor da dívida.'))

    if divida > 0:
        print(f'Total R$ {divida:.2f} Juros: R$ 0,00 Número de parcelas: 1  Valor da Parcela: R$ {divida:.2f}')
        print(f'Total R$ {divida:.2f} Juros: R$ {divida + divida * 10/100:.2f} Número de parcelas 3 Valor da Parcela: R$ {(divida + divida * 10/100)/3:.2f}')
        print(f'Total R$ {divida:.2f} Juros: R$ {divida + divida * 15/100:.2f} Número de parcelas 6 Valor da Parcela: R$ {(divida + divida * 15/100)/6:.2f}')
        print(f'Total R$ {divida:.2f} Juros: R$ {divida + divida * 20/100:.2f} Número de parcelas 9 Valor da Parcela: R$ {(divida + divida * 20/100)/9:.2f}')
        print(f'Total R$ {divida:.2f} Juros: R$ {divida + divida * 25/100:.2f} Número de parcelas 12 Valor da Parcela: R$ {(divida + divida * 25/100)/12:.2f}')
    else:
        print('Valor Incorreto')    