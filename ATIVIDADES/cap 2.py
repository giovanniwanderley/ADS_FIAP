contadora = 0 
numero = int(input('Por favor, insira o número da tabuada'))
while contadora <= 10:
    resultado = numero * contadora
    print (f'{numero} X {contadora} = {resultado}')
    contadora = contadora + 1  