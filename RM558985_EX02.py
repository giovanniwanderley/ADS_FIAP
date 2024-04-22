""" A compra de um veículo pode ser realizada parcelada. Crie um programa 
que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, 
quantidade de parcelas e valor da parcela. Considere o seguinte:
a) O preço final para compra à vista tem um desconto de 20%:
b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60:
Os percentuais de acréscimo seguem na tabela abaixo:"""

valor_carro = int(input('Digite o valor do carro'))


n_parcelas = 1
for x in range (6,61,6):
    match n_parcelas:
        case 1: 
            print(f'o preço final com desconto de 20% é de R${valor_carro * 0.80} em uma parcela de {valor_carro * 0.80}' )
        case 6:
            print(f'o preço final parcelado em é de R$ {(valor_carro * 1.03)} com parcelas de  {(valor_carro * 1.03)/6}' )
            break
        case 12:
            print(f'o valor da parcela é de {(valor_carro * 1.06)/12} com parcelas de  {(valor_carro * 1.06)/12}' )  
            break
        case 18:
            print(f'o valor da parcela é de {(valor_carro * 1.09)/18} com parcelas de  {(valor_carro * 1.09)/18}' )  
            break  
        case 24:
            print(f'o valor da parcela é de {(valor_carro * 1.12)/24} com parcelas de  {(valor_carro * 1.12)/24}' )    
            break
        case 30:
            print(f'o valor da parcela é de {(valor_carro * 1.15)/30} com parcelas de  {(valor_carro * 1.15)/30}' )
            break
        case 36:
            print(f'o valor da parcela é de {(valor_carro * 1.18)/36} com parcelas de  {(valor_carro * 1.18)/36}' )
            break
        case 42:
            print(f'o valor da parcela é de {(valor_carro * 1.21)/42} com parcelas de  {(valor_carro * 1.21)/42}' )
            break
        case 48:
            print(f'o valor da parcela é de {(valor_carro * 1.24)/48} com parcelas de  {(valor_carro * 1.24)/48}' )
            break
        case 54:
            print(f'o valor da parcela é de {(valor_carro * 1.27)/54} com parcelas de  {(valor_carro * 1.27)/54}')
            break
        case 60:
            print(f'o valor da parcela é de {(valor_carro * 1.3)/60} com parcelas de  {(valor_carro * 1.3)/60}' )          
            break              
        case _:
            print('Opção inválida')
            break
