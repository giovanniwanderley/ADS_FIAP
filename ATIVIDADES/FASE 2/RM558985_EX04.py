#Aluno Giovanni Assunção Wanderley RM 558985

opcao_investimento = 0
numero_dias = int(0) 


while opcao_investimento == 1 or 2 or 3: 
    opcao_investimento = int(input('Digite o número referente ao investimento que deseja resgatar: \n\n1- CDB\n2- LC1\n3- LCA:  '))
    if opcao_investimento == 1:
        valor_resgate = float(input('Digite o valor a ser resgatado: '))
        numero_dias = int(input('Digite quanto tempo o valor ficou aplicado: '))
        if numero_dias <181:
            print(f'O VALOR A SER COBRADO DE IR É DE R$ {valor_resgate * 22.5/100:.2f}\nO VALOR LIQUIDO RESGATADO SERÁ R$ {valor_resgate - valor_resgate * 22.5/100}')
        elif numero_dias <361:
             print(f'O VALOR A SER COBRADO DE IR É DE R$ {valor_resgate * 20/100:.2f}\nO VALOR LIQUIDO RESGATADO SERÁ R$ {valor_resgate - valor_resgate * 20/100}')
        elif  numero_dias < 721:   
            print(f'O VALOR A SER COBRADO DE IR É DE R$ {valor_resgate * 17.5/100:.2f}\nO VALOR LIQUIDO RESGATADO SERÁ R$ {valor_resgate - valor_resgate * 17.5/100}')
        elif numero_dias > 720:
            print(f'O VALOR A SER COBRADO DE IR É DE R$ {valor_resgate * 15/100:.2f}\nO VALOR LIQUIDO RESGATADO SERÁ R$ {valor_resgate - valor_resgate * 15/100}')
    elif opcao_investimento == 2 or 3:
        valor_resgate = float(input('Digite o valor a ser resgatado: '))
        print(f'O VALOR A SER COBRADO DE IR É DE R$ 0.00 \nO VALOR LIQUIDO RESGATADO SERÁ R$ {valor_resgate:.2f}')
    else:
        print('Número inválido')       