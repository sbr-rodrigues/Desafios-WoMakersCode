frase = str(input('Qual é a frase: ')).strip().upper()
print('Analisando sua frase... ')
vogais = "aeiouAEIOU"
consoantes = []
for letra in frase:
  if letra.isalpha() and letra not in vogais:
    consoantes.append(letra)
print('Consoantes encontras: ',consoantes)