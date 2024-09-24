renda=float(input('Digite sua renda mensal:'))
score=float(input('Digite seu score de crédito:'))
fiad=input('Você tem fiador de crédito?[S/N]:')
if fiad.upper()=='S':
    qtd_fiad=float(input('Digite o score de crédito do fiador:'))
    if qtd_fiad >=700:
        print('Você é elegível para o empréstimo')
    elif renda >= 2000 and score >=600:
      print('Você é elegível para o empréstimo.')
else:
    print('Você não é elegível para o empréstimo.')
    print("Arthur esteve aqui")