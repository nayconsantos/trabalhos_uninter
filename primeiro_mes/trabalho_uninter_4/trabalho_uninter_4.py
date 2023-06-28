listaPecas = []#lista que irá armazenar os dados das peças cadrastradas
def cadastrarPeca(codigo):#função de cadstrar peças nela, o usuario pode cadastrar quantos itens ele quiser!
  print('Você selecionou a opção de Cadastrar Peça')#não porque vai ter um while e sim porque ele pode selecionar a opção!
  print(f'O código da peça é: {codigo:0>3}')
  nome = input('Por favor entre com o NOME da peça: ')
  fabricante = input('Por favor entre com o FABRICANTE da peça: ')
  valor = float(input('Por favor entre com o VALOR R$ da peça: '))
  dicionarioPecas = {'codigo'   : codigo,
                     'nome' : nome,
                     'fabricante': fabricante,
                    'valor': valor}
  listaPecas.append(dicionarioPecas.copy())#adiona uma copia do dicionario na lista em questão


def consultarPeca():#Do mesmo modo termos a def de consultas, para consultarmos os itens cadastrados,
                    #na mesma podemos obter os itens de formas diferentes seja por codigo ou ate mesmo por nome da fabricante 
  while True:
    try:
      print('Você Selecionou a Opção de Consultar Peças')
      opConsultar = int(input('Entre com a opção desejada\n1- Consultar Todas as Peças\n2- Consultar Peças por Código\n3- Consultar Peças por Fabricante\n4- Retornar\n-->'))
      if opConsultar == 1:#consultar todos os itens cadastrado, vai aperecer todos .
        print('-' * 20)
        for pecas in listaPecas:
            for key, value in pecas.items():
              print(f'{key} : {value}')#retorna todos os valores dos itens cadastrados
            print('-' * 20)
      elif opConsultar == 2:
        print('Você Selecionou a Opção Peças por Código')
        entrada = int(input('Digite o Código: '))#consulta por codigo
        print('-' * 20)
        for pecas in listaPecas:
          if(pecas['codigo'] == entrada):
            for key, value in pecas.items():
              print(f'{key} : {value}')#retorna apenas o item com o codigo certo, ação unica se errar ou não tiver esse codigo cadastrado, tera mensagem de erro
            print('-' * 20)
      elif opConsultar == 3:
        print('Você Selecionou a Opção Peças por Fabricante')
        entrada = input('Digite o Fabricante: ')#da mesma forma por codigo, se for digitada uma marca que não exister retornara mensagem de erro
        print('-' * 20)
        for pecas in listaPecas:
          if(pecas['fabricante'] == entrada):
            for key, value in pecas.items():
              print(f'{key} : {value}')
            print('-' * 20)
      elif opConsultar == 4:#volta para o inicio
        break
      else:
        print('Por favor digite somente o que pede')
        continue
    except ValueError:#caso digite opções invalidas
      print('Por Favor pare de digitar números que não existe...')
      continue

    
def removerPeca():#remove itens que o usuario acho que não mais deseja utilizar, ou se quer atualizar preço seria uma boa uma opção de atualizar produto
    print('Você Selecionou a Opção de Remover Peça')
    entrada = int(input('Digite o Código da peça a ser removida: '))#pede codigo do produto a ser removido
    for pecas in listaPecas:
      if(pecas['codigo'] == entrada):
        listaPecas.remove(pecas)
    else:
      print('Você removeu o código.')
print('Bem-vindo ao Controle de Estoque da Bicicletaria do José Naycon Dos Santos Silva')#Identificação pessoal/inicio/boas vindas
registroPecas = 0
while True:
    try:
      opcao = int(input('Escolha a opção desejada:\n1- Cadastrar Peças\n2- Consultar Peças\n3- Remover Peças\n4- Sair\n--> '))#menu de opções de inicio
      if opcao == 1: 
        registroPecas = registroPecas + 1
        cadastrarPeca(registroPecas)
      elif opcao == 2:
        consultarPeca()
      elif opcao == 3:
        removerPeca()
      elif opcao == 4:
        print('Programa finalizado')
        break
      else:
        print('Digite somente uma das opções do MENU')
        continue
    except ValueError:#caso digite opções invalidas
        print('Pare de digitar números que não existe...')