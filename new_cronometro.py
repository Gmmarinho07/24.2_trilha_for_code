import os, time

def iniv():
    segundo = 0
    minuto = 0
    hora = 0
    return segundo, minuto, hora

def turn60(segundo, minuto, hora):
    if segundo == 60:
        if minuto == 59:
            minuto = 0
            segundo = 0
            hora += 1

        else:
            segundo = 0
            minuto += 1

    return (segundo, minuto, hora)

def printh(segundo, minuto, hora):
    if segundo < 10:
        segundo = f'0{segundo}'

        if minuto < 10:
            minuto = f'0{minuto}'

        if hora < 10:
            hora = f'0{hora}'

    print(f'{hora}:{minuto}:{segundo}')

    return segundo, minuto, hora


def main():
    segundo, minuto, hora = iniv()

    while True:
        os.system('cls')

        segundo, minuto, hora = turn60(segundo, minuto, hora)
        printh(segundo, minuto, hora)

        time.sleep(1)
        segundo += 1


main()
