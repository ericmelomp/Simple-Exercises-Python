primeironome = str(input('Qual o seu primeiro nome? '))
sobrenome = str(input('Qual o seu sobrenome? '))
ultimonome = str(input('Qual o seu último nome? '))

bornyear = int(input('Em que ano você nasceu? '))
currentyear = int(input('Em que ano estamos? '))
age = currentyear-bornyear

print('Seu nome completo é',primeironome,sobrenome,ultimonome)
print('Você tem ou fará {} anos de idade'.format(age))