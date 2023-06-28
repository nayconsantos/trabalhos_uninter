print(25*'*','Bem-vindo a Companhia de Logistica José Naycon Dos Santos Silva S.A',25*'*')#identificador pessoal/boas vindas/
print('')
print(50*' ','TABELA DE VALORES:\n')#menu de opções para informar as dimensões das cargas a serem transportadas
print(129*'_')
print('|------Dimensões cm³------|--Valor--|   |-------Peso-------|Multiplicador|   |----------------Rotas---------------|Multiplicador|')
print('|Volume menor que    1.000| R$:10.00|   |  Menor que 100G  |      1x     |   |RS - De Rio de Janeiro até São Paulo|      1x     |')
print('|1000  <= volume <  10.000| R$:20.00|   | 100G entre < 1kg |      1.5x   |   |SR - De São Paulo até Rio de Janeiro|      1x     |')
print('|10000 <= volume <  30.000| R$:30.00|   | 1kg entre < 10kg |	     2x     |   |BS - De Brasília até São Paulo      |      1.2x   |')
print('|30000 <= volume < 100.000| R$:50.00|   |10kg  entre < 30kg|      3x     |   |SB - De São Paulo até Brasília      |      1.2x   |')   
print('|Volume maior que  100.000| Ñ aceito|   |  Maior que 30Kg  | Não é aceito|   |BR - De Brasília até Rio de Janeiro |      1.5x   |')
print('|'+ 127*'_'+'|')
print('')
#inicio da função para informas a(s) dimensões do produto(s) a serem transportados.
def dimensoesObjeto():
    while True:
     try:
        dim1 = int(input('Digite o comprimento da carga em cm: '))
        dim2 = int(input('Digite a largura da carga em cm: '))
        dim3 = int(input('Digite a altura da carga em cm: '))
        mult = float(dim1 * dim2 * dim3)
        tam = mult
        print (f'O volume do objeto é (em cm³): {tam}')
        if(tam <= 1000):
          return 10.00
        elif(tam >= 1001) and (tam < 10000):
          return 20.00
        elif(tam >= 10001) and (tam < 30000):
          return 30.00
        elif(tam >= 30001) and (tam < 100000):
          return 50.00
        else:
            print('Não aceitamos objetos com dimensões tão grandes!')
            print('Entre com as dimensões desejadas novamente!')
            continue
     except ValueError:
        print('Você digitou alguma dimensão não númerico!')
        print('Entre com as dimensões desejadas novamente!')
        continue
#fim da função de informar a(s) dimenções do produto(s) a serem transportados.   

#inicio da função peso, cliente vai informar o peso da mercadoria a ser transportada!
def pesoObjeto():
    while True:
     try:
        peso =float(input('Digite o peso da carga em kg: '))
        peso2 = peso
        if(peso2 <= 0.1):
         return 1
        elif(peso2 <= 1) and (peso2 >= 0.11):
         return 1.5
        elif(peso2 <= 10) and (peso2 >= 1.10):
         return 2
        elif(peso2 <= 30) and (peso2 >= 10.1):
         return 3
        else:
            print('Não aceitamos objetos tão pesados!')
            continue
     except ValueError:
       print('Você digitou peso do objeto com valor não numérico \nPor favor entre com o peso desejado novamente')
       continue
#fim da função peso.
     
# inicio da função de rota com os valores/dados para onde transportar
def rotaObjeto():
    while True:
     try:
        rota = (input('Selecione a rota: \nBR - De Brasília para Rio de Janeiro\nBS - De Brasília para São Paulo\nRB - De Rio de Janeiro para Brasília\nRS - De Rio de Janeiro para São Paulo\nSR - De São Paulo para Rio de Janeiro\n>> ')).upper()
        r = rota
        if(r == 'RS'):
         return 1
        elif(r == 'SR'):
         return 1
        elif(r == 'BS'):
         return 1.2
        elif(r == 'SB'):
         return 1.2
        elif (r == 'BR'):
            return 1.5
        elif (r == 'RB'):
            return 1.5
        else:
            print('!!!Ops!!! Você digitou uma rota que não existe!')
            continue
     except ValueError:
       print('!!!Ops!!! Está rota não existe \nPor favor entre com a rota desejada novamente: ')
       continue
    #fim da função da rota a ser traçada 

dimf = dimensoesObjeto()#chamando a função, para efetuar a execução, atribida a uma variavel.
pesof = pesoObjeto()#chamando a função, para efetuar a execução, atribuida a uma variavel.
rotf = rotaObjeto()#chamando a função, para efetuar a execução, atriuida a uma variavel.
total_t= dimf*pesof*rotf#total final atribuido as funções anteriores, com o proposito de efetuar o calculo mais simples. 
print(f'O total a pagar ficou R$:{total_t:.2f} (Dimensões {dimf} * Peso {pesof} * Rota {rotf})')#resultado final , aqui vai aparecer o total final do serviço a ser cobrado.

#não sou muito experiente, por isso o programa possivelmente vai ter varios eros pesso desculpas e paciencia
#pois é a minha primeira vez como programador, espero que entenda!