from time import sleep


def aumentar(n, p, formata=False):
    valor = n + (n * (p/100))
    if formata:
        return moeda(valor)
    else:
        return valor


def diminuir(n, p, formata=False):
    valor = n - (n * (p/100))
    if formata:
        return moeda(valor)
    else:
        return valor


def dobro(n, formata=False):
    valor = n*2
    if formata:
        return moeda(valor)
    else:
        return valor


def metade(n, formata=False):
    valor = n/2
    if formata:
        return moeda(valor)
    else:
        return valor


def moeda(n):
    num = str(f'R${n:.2f}')
    return num


def resumo(x, y, z):
    print(cor[0], end='')
    print('-'*50)
    print(f'{"RESUMO DE VALORES":^50}')
    print('-'*50)
    print(cor[1], end='')
    sleep(.5)
    print(f'O valor digitado é R${x:.2f}')
    sleep(.5)
    print(f'O valor com acréscimo de {y}% é {aumentar(x, y, formata=True)}')
    sleep(.5)
    print(f'O valor com desconto de {z}% é {diminuir(x, z, formata=True)}')
    sleep(.5)
    print(f'O dobro de R${x:.2f} é {dobro(x, formata=True)}')
    sleep(.5)
    print(f'A metade de R${x:.2f} é {metade(x, formata=True)}')

cor = ('\033[30;42m',     # 2 - verde
       '\033[7;30m'       # 6 - branco
        )




