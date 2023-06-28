print('Bem vindo a Lanchonete do José Naycon Dos Santos Silva')#Identificador pessoal/boas vindas/inicio...
print(20*'*','CARDÁPIO',27*'*')
print('|Código|     |       Descrição       |       |   Valor  |')#menu com opções de lanches disponiveis...
print('| 100  |     |    Cachorro-Quente    |       |  R$9,00  |')
print('| 101  |     | Cachorro-Quente Duplo |       |  R$11,00 |')
print('| 102  |     |         X_Egg         |       |  R$12,00 |')
print('| 103  |     |        X-Salada       |       |  R$13,00 |')
print('| 104  |     |        X-Bacon        |       |  R$14,00 |')
print('| 105  |     |         X-Tudo        |       |  R$17,00 |')
print('| 200  |     |   Refrigerante Lata   |       |  R$5,00  |')
print('| 201  |     |      Chá Gelado       |       |  R$4,00  |')    

valortotal=0 #valor x/total ao final do encerramento do pedido

while True:
    #Inicio da validação de acordo com o codigo do cardapio acima!
    #uma opção de recusar strings e floats seria uma boa, resolvi não encorpar...
    codigo = int(input('\nEntre com o código do lanche desejado: '))
    if codigo == 100:
       valortotal += 9
       print('Você pediu um Cachorro-Quente no valor de R$9,00')
    elif codigo == 101:
       valortotal += 11
       print('Você pediu um Cachorro-Quente Duplo no valor de R$11,00')
    elif codigo == 102:
       valortotal += 12
       print('Você pediu um X-Egg no valor de R$12,00')
    elif codigo == 103:
       valortotal += 13
       print('Você pediu um X-Salada no valor de R$13,00')
    elif codigo == 104:
       valortotal += 14
       print('Você pediu um X-Bacon no valor de R$14,00')
    elif codigo == 105:
       valortotal+=17
       print('Você pediu um X-Tudo no valor de R$17,00')
    elif codigo == 200:
       valortotal+=5
       print('Você pediu um Refrigerante Lata no valor de R$5,00')
    elif codigo == 201:
       valortotal += 4
       print('Você pediu um Chá Gelado no valor de R$4,00')
    else:
       print('Este código de lanche não existe, digite uma opção válida')
       continue
    #fim da validação do pedido de acordo com o codigo do cardapio acima!
    #OBS: voltara para o inicio caso não digite um codigo valido!

    op = input('Deseja fazer um novo pedido?[S/N] ').upper().strip()#opção para validar se o cliente quer pedir mais alguma coisaou encerrar o pedido
    while op != 'N' and op != 'S':
       op = input('Deseja fazer um novo pedido?[S/N] ').upper().strip()#não achei muito prqatico esse while dentro de outro porém, eu sou iniciante e não encontrei outra resposta para resolver essa questão
    if op == 'S':
        continue
    elif op == 'N':
        print('Você encerrou o pedido!')
        break
print(f'Valor total do pedido a ser pago: R$ {valortotal:.2f}')#fim do progama, aqui irá mostrar o valor total aser pago.
