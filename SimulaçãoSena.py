from random import sample
from time import sleep

def obter_numero_valido():
    while True:
        entrada = input("Digite uma dezena (01-60): ")
        if len(entrada) != 2 or not entrada.isdigit() or int(entrada) < 1 or int(entrada) > 60:
            print('Dezenas precisam ser de 01 a 60. Tente novamente.')
        else:
            return int(entrada)

def verificar_resultado(sorteio, escolhidos):
    numeros_em_comum = [numero for numero in sorteio if numero in escolhidos]
    numeros_em_comum.sort()

    if not numeros_em_comum:
        print('Não foi dessa vez.')
    else:
        print("Os números em comum foram:", numeros_em_comum)

    acertos = len(numeros_em_comum)
    if acertos == 1:
        print('Você acertou 1 dezena.')
    elif acertos == 2:
        print('Você acertou 2 dezenas.')
    elif acertos == 3:
        print('Você acertou 3 dezenas.')
    elif acertos == 4:
        print('Parabéns! Você acertou a quadra!')
    elif acertos == 5:
        print('Parabéns! Foi quase. Você acertou a quina!')
    elif acertos == 6:
        print('TEMOS UM NOVO MILIONÁRIO(A)! Você acertou a sena.')

def main():
    print("Para esse sorteio, você precisa escolher 6 dezenas diferentes entre 01 e 60.")
    print("Vamos lá!\n")

    sorteio = sample(range(1, 61), 6)
    escolhidos = []

    for i in range(1, 7):
        print(f'Dezena {i}:')
        dezena = obter_numero_valido()
        escolhidos.append(dezena)

    print("\nAguarde...")
    sleep(2)

    sorteio.sort()
    print("Os números sorteados foram:", sorteio)
    escolhidos.sort()
    print("Você escolheu:", escolhidos)

    verificar_resultado(sorteio, escolhidos)

if __name__ == "__main__":
    main()
