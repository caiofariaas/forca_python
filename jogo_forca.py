letras_usuario = []
worl = True
chances = 6

palavra = input("Digite uma palava para começar: ")
palavra = palavra.lower()
dica = input("De uma dica ao usuário: ")
print("-=" * 15)
print("\nBem vindo ao jogo da forca!!\n")
print("-=" * 15 + "\n\n")

while True:
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end='')
        else:
            print("_", end="")
    print(f"\nDica: {dica}")
    print(f"Letras ja usadas: {letras_usuario}")
    tentativa = input("\nDigite uma letra: ")
    letras_usuario.append(tentativa.lower())

    if tentativa.lower() not in palavra:
        chances -= 1
        print(f"Essa letra não se encontra na palavra! Você tem {chances} chances!")

    if chances == 6:
        print('''
             +---+
                 |
                 |
                 |
                 |
          ======== 
                 ''')
    elif chances == 5:
        print('''
            +---+
            0   |
                |
                |
                |
         ======== 
                ''')
    elif chances == 4:
        print('''
            +---+
            0   |
            |   |
                |
                |
         ======== 
                ''')
    elif chances == 3:
        print('''
            +---+
            0   |
            |\  |
                |
                |
         ======== 
                ''')
    elif chances == 2:
        print('''
            +---+
            0   |
           /|\  |
                |
                |
         ======== 
                ''')
    elif chances == 1:
        print('''
            +---+
            0   |
           /|\  |
           /    |
                |
         ======== 
                ''')

    worl = True

    for letra in palavra:
        if letra.lower() not in letras_usuario:
            worl = False

    if chances == 0 or worl:
        break

if worl:
    print("\n" + "-=" * 20)
    print(f"\nParabéns, você ganhou! A palavra era '{palavra}'\n")
    print("-=" * 20)
else:
    print("\n" + "-=" * 20)
    print('''
        +---+
        0   |
       /|\  |
       / \  |
            |
     ======== 
            ''')
    print(f"Você perdeu! A palavra certa era '{palavra}'")
    print("-=" * 20)
