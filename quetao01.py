"""
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom
"""

a = float(input(" Qual o valor da conta a ser paga? "))

b = a + (a * 0.10)

print(f"O valor da conta a ser paga é de: {b} " )
