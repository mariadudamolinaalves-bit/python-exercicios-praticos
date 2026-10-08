# exercicio 3 
# Desafio 3: Comissão de uma venda
# Valor negativo: exiba “Valor inválido”, sem calcular comissão.
# De R$ 0 até menos de R$ 100: sem comissão.
# De R$ 100 até menos de R$ 500: comissão de 1%.
# A partir de R$ 500: comissão de 5%.
valor_venda = float(input("Digite o valor da venda: "))
if valor_venda < 0 :
    print("Valor inválido")
elif valor_venda < 100 :
    print ("Sem comissão")
elif valor_venda < 500 :
    print("Comissão de 1%")
else:
    print("Comissão de 5%")
    

