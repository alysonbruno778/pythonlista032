"""
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
"""

a = float(input("Qual o seu peso em quilos? "))
b = float(input("Qual a sua altura em metros? "))

c = a * 1000
d = b * 100

print(f"Seu peso em gramas é de: {c} ")
print(f"Sua altura em centímetros é de: {d}")