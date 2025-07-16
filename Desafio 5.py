peso =float(input('Qual é o seu peso? (kg)' ))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.2f}')
if imc < 18.5:
  print('Você está abaixo do peso ideal.')
elif 18.5<= imc < 24.9:
  print('Você está com sobrepeso.')
elif imc >=30:
  print('Você está obeso')