"""
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês
"""

nome = input("Informe o seu nome: ")
sf = float(input("Informe o seu salário fixo: "))
vend = int(input("Valor em dinheiro das vendas que efetuadas no mês: R$"))
com = (vend * 0.15)
sc = com + sf

print(f"O nome do funcionário é: {nome}")
print(f"O salário fixo do funcionáro é: R${sf}")
print(f"A comissão do funcionário foi de: R${com}")
print(f"O salário completo do funcionário foi de: R${sc}")