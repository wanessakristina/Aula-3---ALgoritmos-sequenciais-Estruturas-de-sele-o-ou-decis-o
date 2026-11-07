# Exercício 6(5) (Refatorado): Condicional de Múltipla Escolha (elif)

print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Qual sua escolha? '))
qtd = int(input('Quantas unidades? '))

# Estrutura limpa usando elif (sem aninhamento profundo)
if produto == 1:
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maçãs. Total a pagar: {pagar:.2f}')
elif produto == 2:
    pagar = qtd * 3.6
    print(f'Você comprou {qtd} laranjas. Total a pagar: {pagar:.2f}')
elif produto == 3:
    pagar = qtd * 1.85
    print(f'Você comprou {qtd} bananas. Total a pagar: {pagar:.2f}')
else:
    print('Produto inexistente!')