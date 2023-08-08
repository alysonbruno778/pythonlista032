"""
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros.
"""

a = float(input("Qual o seu peso em quilos? "))
b = float(input("Qual a sua altura em metros? "))

IMC = a / b

print(f"seu índice de massa corporal(imc) é: {IMC}")