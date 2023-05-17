

while True:
    try:
        n = int(input('digite um numero inteiro: '))
    except:
        print('valor inválido')
    else:
        print(f'O valor digitado é {n}')
        break



while True:
    try:
        p = int(input('digite um numero inteiro'))
    except ValueError:
        print('valor inválido')
    except KeyboardInterrupt:
        print(f'\nUsuário interropeu a execução')
        break
    else:
        print(f'O valor digitado é: {p}')
        break

