print('Bem-vindo ao Entrega Fast!')
print('1 - Até 1Kg => R$5,00')
print('2 - 1 a 5Kg => R$10,00')
print('3 - Acima de 5Kg => R$20,00')
escolha = int(input('Selecione o peso do produto para avaliar o custo do frete '))
if escolha == 1:
    print('O valor do frete é de R$5,00')
elif escolha ==2:
    print('O valor do frete é de R$10,00')
else:
    print('O valor do frete é de R$20,00')
print('Obrigado pela preferência')