#Uma função com variável global afeta variáveis fora da função

def teste(b):
    global a
    a = 10
    b = b + 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")

#principal
a = 5
teste(a)
print(f"A fora vale {a}")