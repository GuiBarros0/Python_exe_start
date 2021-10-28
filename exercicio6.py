nomevendedor=input('cadastre o nome do vendedor: ')
preco=float(input('informe o preço da peça: '))
quantidade=int(input('digita quatidade de peças: '))
total=preco*quantidade
comissao=total*5/100
print('a comissão do funcionario: ',nomevendedor)
print('é R$',comissao)
