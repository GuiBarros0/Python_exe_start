nome=input('informe o nome do funcionario: ')
salariobase=float(input('informe o salario base do funcionario R$'))
imposto=salariobase*3/100
gratis=salariobase*5/100
salarioliquido = salariobase + gratis - imposto
print('seu salario final desse mês é de R$',salarioliquido,)
