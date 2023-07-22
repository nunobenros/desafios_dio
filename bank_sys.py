
#Nuno Silas Benrós Santos
"""Fomos contratados por um grande banco para desenvolver o seu novo sistema.
 Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
 Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.
"""

#entrada=input("""Olá!
#Qual a operação que deseja efetuar:
#    1- Depósito
#    2- Saque
#    3-Extrato
#    0-Sair """)
#
#if entrada=='1':
#    dep_real=0
#    dep_try= int(input('Qual o valor que deseja depositar?'))
#    if dep_try <=0:
#        print('Não é possível esse depósito')
#    else:
#        dep_real+=dep_try
#
#print(dep_real)


menu = """ Qual a operação deseja efetuar:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
"""
saldo = 0
limite = 500
extrato= ""
numero_saques =3
numero_saques_try=0

while True:

    opcao= input(menu)

    if opcao == "d":
        dep=int(input('Qual o valor do depósito pretendido?'))
        if dep <=0 :
            print("Não é possível realizar esse depósito!")
        else:
            saldo+=dep
        print(f"""Deposito efetuado 
              Saldo:{saldo} R$ \n""")
        extrato +=f'Depósito: R$ {dep:.2f}\n'
        1000
        

    elif opcao == "s":
        saq=int(input('Qual o valor do saque pretendido?'))
        
        if numero_saques_try > numero_saques :
            print(f"Não é possível realizar o saque, é possível apenas {numero_saques} tentativas de saque no dia")

        elif saq > 500:
            print(f'Não é possível realizar esse saque, o valor máximo é de {limite} R$00')
        elif saq>saldo:
            print(f'Não é possível realizar o saque de {saq}R$ pois o saldo é insuficiente')
        else:
            saldo+= -saq
            print(f'Saque de {saq} efetuado. \n Saldo disponível: {saldo}')
            numero_saques_try+=1
            extrato+= f'Saque: R$ {dep:.2f}\n'

    elif opcao =='e':
        print("Não existem transações " if not extrato else extrato)

    elif opcao =="q":
        break


