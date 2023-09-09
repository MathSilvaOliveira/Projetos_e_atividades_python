'''''
Imagine que você está trabalhando com os dados de vendas de uma loja. Você recebeu uma 
lista de tuplas, onde cada tupla contém informações sobre uma venda, incluindo o nome do 
produto, a quantidade vendida e o preço unitário do produto. Sua tarefa é calcular algumas 
estatísticas com base nessas informações.
Seu desafio é o seguinte:
● Calcule o total de vendas para cada produto e apresente os resultados em uma lista de 
tuplas, onde cada tupla contém o nome do produto e o total de vendas desse produto.
● Calcule o total geral de vendas (a soma de todas as vendas) e o preço médio dos 
produtos vendidos.
● Encontre o produto mais vendido (aquele com o maior total de vendas) e o produto 
menos vendido (aquele com o menor total de vendas).
Apresente todos os resultados de maneira legível e organizada.
'''

vendas = [
      ("Produto A", 10, 15.99),
      ("Produto B", 5, 26.50),
      ("Produto C", 20, 10.99),
      ("Produto A", 8, 10.99),
      ("Produto C", 12, 10.99),
      ("Produto B", 7, 25.50),
]

def totaldevendasdecadaproduto(tupla):
  total_por_produto = {}
  
  for produto, quantidade, preco_unitario in vendas:
      if produto in total_por_produto:
          total_por_produto[produto] += quantidade
      else:
          total_por_produto[produto] = quantidade
  
  for produto, quantidade_total in total_por_produto.items():
      print(f"{produto}, Quantidade Total: {quantidade_total}")


def somadetodasasvendas_e_media(tupla):
      count = len(vendas)
      total = []
      media = []
      
      for c in range(count):
         total.append(vendas[c][1])
         media.append(vendas[c][2])
      print("A soma de todas as vendas:", sum(total))
      print("Preço médio: $", round(sum(total)/len(vendas), 2))



def mais_vendido_e_menos_vendido(tupla):
   mais_vendido = None
   menos_vendido = None
   quantidade_mais_vendido = float("-inf")
   quantidade_menos_vendido = float("inf")

# Crie um dicionário para rastrear as quantidades totais por produto
   total_vendas_por_produto = {}

   for produto, quantidade, _ in vendas:
       # Atualize o total de vendas para cada produto
       if produto in total_vendas_por_produto:
           total_vendas_por_produto[produto] += quantidade
       else:
           total_vendas_por_produto[produto] = quantidade
   
       # Atualize o produto mais vendido e menos vendido, se necessário
       if quantidade > quantidade_mais_vendido:
           mais_vendido = produto
           quantidade_mais_vendido = quantidade
       elif quantidade < quantidade_menos_vendido:
           menos_vendido = produto
           quantidade_menos_vendido = quantidade

   print(f"Produto mais vendido: {mais_vendido}, Total de vendas: {total_vendas_por_produto[mais_vendido]}")
   print(f"Produto menos vendido: {menos_vendido}, Total de vendas: {total_vendas_por_produto[menos_vendido]}")


#Chamando as funçôes
totaldevendasdecadaproduto(vendas)

somadetodasasvendas_e_media(vendas)

mais_vendido_e_menos_vendido(vendas)
