usuarios={}
opcao=input('O que deseja realizar?' 
+ 
            '<I> - Para Inserir um usuário' 
+ 
            '<P> - Para Pesquisar um usuário'
+  
           '<E>' ' Para Excluir um usuário' 
+
            '<L> - Para Listar um usuário: ').upper()
while opcao=='I' or opcao=='P' or opcao=='E' or opcao=='L':
    if opcao =='I':
        chave=input('Digite o login: ').upper()
        nome=input('Digite o nome: ').upper()
        data=input('Digite a data: ').upper()
        estacao=input('Digite a estacao: ').upper()
        usuarios