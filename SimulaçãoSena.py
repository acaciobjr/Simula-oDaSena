from random import sample
from time import sleep

sorteio = sample(range(0, 60), 6)
l1 = []


print("Para esse sorteio você precisa escolher 6 dezenas diferentes entre 01 e 60.")
print("Vamos lá!")

while True:
        dezena1 = input("primeira dezena: ")

        if len(dezena1) != 2:
            print('Dezenas possuem 2 algarismos. Digite novamente:')
        elif (int(dezena1) > int(60)):
                print('As dezenas precisam ser entre 01 e 60')
                dezena1 = input("primeira dezena: ")
        else: break
while True:
        dezena2 = input("segunda dezena: ")
        if len(dezena2) !=2:
            print('Dezenas possuem 2 algarismos. Digite novamente:')
        elif (int(dezena2) > int(60)):
                print('As dezenas precisam ser entre 01 e 60')
                print('digite novamente.')
        else:
            break
while True:
        dezena3 = input("terceira dezena: ")
        if len(dezena3) !=2:
            print('Dezenas possuem 2 algarismos. Digite novamente:')
        elif (int(dezena3) > int(60)):
                print('As dezenas precisam ser entre 01 e 60')
                print('digite novamente.')
        else:
            break
while True:
        dezena4 = input("quarta dezena: ")
        if len(dezena4) !=2:
            print('Dezenas possuem 2 algarismos. Digite novamente:')
        elif (int(dezena4) > int(60)):
            print('As dezenas precisam ser entre 01 e 60')
            print('digite novamente.')
        else:
            break
while True:
    dezena5 = input("quinta dezena: ")
    if len(dezena5) !=2:
        print('Dezenas possuem 2 algarismos. Digite novamente:')
    elif (int(dezena5) > int(60)):
        print('As dezenas precisam ser entre 01 e 60')
        print('digite novamente.')
    else:
        break
while True:
    dezena6 = input("sexta dezena: ")
    if len(dezena6) !=2:
        print('Dezenas possuem 2 algarismos. Digite novamente:')
    elif (int(dezena6) > int(60)):
        print('As dezenas precisam ser entre 01 e 60')
        print('digite novamente.')
    else:
        break


escolhidos = [int(dezena1), int(dezena2), int(dezena3), int(dezena4), int(dezena5), int(dezena6)]
print("aguarde..")
sleep(2)

print("Os números sorteados foram: ", sorteio)
print("Você escolheu: ", escolhidos)

def findDuplicate(self, nums):
      hare = nums[0]
      tortoise = nums[0]
      while True:
         hare = nums[nums[hare]]
         tortoise = nums[tortoise]
         if hare == tortoise:
            break
      ptr = nums[0]
      while ptr!=tortoise:
         ptr = nums[ptr]
         tortoise = nums[tortoise]
      return ptr


def L3():
    for i in sorteio:
        if i in escolhidos:
            l1.append(i)
    return l1


if L3() == []:
    print('não foi dessa vez')
else:
    print("O numeros em comum foram: ", l1)
