#setando funcion
def conta_a_na_string(texto):
#contando quantia de 'a'
    count = texto.lower().count('a')
#retorno
    return f"A letra 'a' aparece {count} vezes na string."

#texto pode ser mudado pelo cliente
texto_informado = "Angelicalmente"
#print final
print(conta_a_na_string(texto_informado))