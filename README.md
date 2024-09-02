*Teste-Target*

*Estágio em Desenvolvimento Target Sistemas*

*Etapas dos Desafios:*

*1) Verificação de número na sequência de Fibonacci*

Objetivo: Determinar se um número informado pertence ou não à sequência de Fibonacci.
Passos:

1)Definição da Sequência, a sequência é definida como 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., onde cada número é a soma dos dois números anteriores.
2)Inicialização de Valores, começamos com os dois primeiros números da sequência: a = 0 e b = 1.
3)Geração de sequência, usar um loop para gerar a sequência:

Enquanto a (o número atual na sequência) for menor que o número informado (numero), atualizamos os valores:
a é definido como b (o próximo número da sequência).
b é definido como a soma de a e b (o novo número na sequência).
Verificação: Após o loop, verificamos se a (o número mais recente gerado na sequência) é igual ao número informado. Se for, o número pertence à sequência; caso contrário, não pertence.


*2) Verificação da letra 'a' em uma string*
Objetivo: Contar quantas vezes a letra 'a' (maiúscula ou minúscula) aparece em uma string.
Passos:

1)Entrada da String, recebe a string para ser verificada.
2)Contagem das Letras, convertamos a string para minúsculas usando (texto.lower()) para garantir que a contagem não seja sensível a maiúsculas/minúsculas, em seguida, usamos o método (.count('a')) para contar verificar a quatiadade de letras 'a'.
3)Saída, retorna a quantidade de vezes que a letra 'a' aparece na string.
