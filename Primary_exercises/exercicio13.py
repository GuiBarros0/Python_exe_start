deposito=float(input('informe o valor do deposito R$'))
taxa=float(input('informe o valor do taxa R$'))
rendimento=deposito*taxa/100
total=deposito+rendimento
print('seu deposito rendeu',rendimento, 'e seu valor final é de R$',total)
