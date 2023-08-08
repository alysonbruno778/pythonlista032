"""
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número
"""

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))

c = a + b
d = a - b
e = b - a
f = a * b
g = a / b
h = a % b

print(f"O valor da soma dos dois números é de: {c}")
print(f"O valor da subtração do primeiro pelo segundo número é de: {d} ")
print(f"O valor da subtração do segundo pelo primeiro número é de: {e} ")
print(f"O valor da multiplicação entre os dois números é de: {f}")
print(f"O valor da divisão do primeiro pelo segundo número é de: {g} ")
print(f"O valor do resto da divisão do primeiro pelo segundo número é de: {h} ")
