nome=input('informe o nome do funcionario: ')
salario1=float(input('informe o valor do salario do funcionario R$'))
porcento=float(input('informe o porcentual de aumento: '))
aumento=salario1*porcento/100
total=salario1+aumento
print('o valor aumentado foi de R$',aumento, 'e o salario total é de R$',total)
