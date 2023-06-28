print(20*'-','Bem-Vindo ao progama do José Naycon Dos Santos Silva', 20*'-') #Identificação do progama/Inicio também 
valor_produto = float(input('Digite o valor do produto: R$ '))#pede o valor do produto 
qtd_produto = float(input('Digite a quantidade do produto: '))#pede a quantidade do produto em questão 
if 0 <= qtd_produto < 10:#exigencia 1 
   desconto = 0 
elif 10 <= qtd_produto < 100:#exigencia 2 
   desconto = 0.5 
elif 100 <= qtd_produto < 1000:#exigencia 2 
    desconto = 0.10 
else:#exigencia 3 
  desconto = 0.15 
semdesconto =  valor_produto * qtd_produto#retorna valor sem desconto 
comdesconto = semdesconto - semdesconto * desconto#retorna valor com desconto 
print(f'O valor Sem desconto foi R${semdesconto:.2f}')#valor sem o desconto aplicado 
print(f'O valor Com desconto foi R${comdesconto:.2f}   (desconto {desconto:.2f}%)')#valor com desconto aplicado 
