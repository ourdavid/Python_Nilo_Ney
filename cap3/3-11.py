#Faça um programa que solicite o preço de uma mercadoria e o
#percentual de desconto. Exiba o valor do desconto e o preço a pagar.


mercadoria_preco = float(input("Preço da mercadoria: "))
percentual_desconto = float(input("Percentual de desconto: ")) / 100


print(f"Valo da mercadoria: {mercadoria_preco} \n "
      f"valor da desconto: {percentual_desconto * 100}% \n "
      f"valor total {mercadoria_preco - (mercadoria_preco * percentual_desconto)} "
      )