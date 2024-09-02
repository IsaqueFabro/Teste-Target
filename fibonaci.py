#setando funcion
def pertence_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    if a == numero:
#retorno
        return f"O número informado: {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número informado: {numero} não pertence à sequência de Fibonacci."

#numero pode ser mudado pelo cliente
numero_informado = 55
#print final
print(pertence_fibonacci(numero_informado))