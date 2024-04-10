quantidade_colaboradores = int(input('Digite a quantidade de colaboradores que irão participar da votação'))
segunda_feira=0
terca_feira=0
quarta_feira=0
quinta_feira=0
sexta_feira=0
i=0
while i < quantidade_colaboradores:
    dia_escolhido = int(input('Escolha o número que corresponde o dia de sua preferência \n1.Segunda-feira\n2.Terça-feira\n3.Quarta-feira\n4.Quinta-feira\n5.Sexta-feira'))
    i+=1
    if dia_escolhido == 1:
        segunda_feira +=1
    if dia_escolhido == 2:
        terca_feira += 1
    if dia_escolhido == 3:
        quarta_feira+=1       
    if dia_escolhido == 4:
        quinta_feira += 1    
    if dia_escolhido == 5:
        sexta_feira+=1
    if dia_escolhido not in (segunda_feira,terca_feira,quarta_feira, quinta_feira,sexta_feira):
        print('Dia Inválido')
        break
dia_mais_escolhido = max(segunda_feira,terca_feira,quarta_feira,quinta_feira,sexta_feira)
if dia_mais_escolhido == segunda_feira:
    print('O dia mais escolhido foi segunda-feira')
elif dia_mais_escolhido == terca_feira:
    print('O dia mais escolhido foi terça-feira')
elif dia_mais_escolhido == quarta_feira:
    print('O dia mais escolhido foi quarta-feira')    
elif dia_mais_escolhido == quinta_feira:
    print('O dia mais escolhido foi quinta-feira')
elif dia_mais_escolhido == sexta_feira:
    print('O dia mais escolhido foi sexta-feira')
    
