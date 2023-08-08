"""
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações
"""

a = float(input("Informe o valor da uma compra: R$ "))
b = float(input("Informe o número de prestações escolhidas: "))

c = a / b

print(f"o valor de cada uma das prestações é de: {c:.2f}")

