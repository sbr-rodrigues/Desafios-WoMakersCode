from random import randint
computador = randint (1,100)
print("Sou seu computador ... Acabei de pensar em um número entre 1 a 100")
print('Tente adivinhar!')
acertou = False
palpites = 0
while not acertou:
  jogador = int(input("Qual é o seu palpite? "))
  if jogador <1 or jogador >100:
    (print('Número inválido!Digite um valor entre 1 a 100'))
    continue
  palpites +=1
  diferenca = abs(jogador - computador)
  if jogador == computador:
    acertou = True
  elif diferenca > 30:
    print('Muito frio!')
  elif diferenca >=16 and diferenca <=29:
    print('Frio!')
  elif diferenca >=6 and diferenca <=15:
    print('Quente!')
  else:
    print('Muito quente!')
print(f'Parabéns! Você acertou! O número era {computador}! Você venceu!')
print('FIM DE JOGO!')