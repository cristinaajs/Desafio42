#Faça um programa no qual o usuário precisa cadastrar as informações de um produto: 
#código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total da compra.

print("Cadastre seu produto")
codigo = input("Digite o código produto: ")
produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite quantos produtos são: "))
valor = int(input("Digite o preço do produto: "))
resultado = quantidade*valor

print("codigo",codigo,"\nproduto",produto,"\nquantidade",quantidade,"\nvalor unitário: ",valor,"\nvalor final",resultado)