maior = 0
menor = 5
soma = 0
homens = 0
mulheres = 0

for i in range(15):

    altura = float(input("Digite a altura: "))
    genero = input("Digite o gênero (M/F): ")

    if altura > maior:
        maior = altura

    if altura < menor:
        menor = altura

    if genero == "M":
        soma = soma + altura
        homens = homens + 1

    if genero == "F":
        mulheres = mulheres + 1

if homens > 0:
    media = soma / homens
else:
    media = 0
print("Maior altura:", maior)
print("Menor altura:", menor)
print("Média de altura dos homens:", media)
print("Quantidade de mulheres:", mulheres)