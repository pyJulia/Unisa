print('Cálculo do IMC (Índice de Massa Corporal).')
peso = float(input('Qual é o seu peso? (Kg) '))
alt = float(input('Qual é a sua altura? (m) '))
imc = peso / (alt ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc <18.5:
    print('Você está abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >=40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')