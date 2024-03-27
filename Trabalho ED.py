import random

TAM = 4

class Pilha:
    def __init__(self):
        self.topo = -1
        self.item = [None] * TAM

def inicializa_pilha():
    return Pilha()

def pilha_vazia(p):
    return p.topo == -1

def pilha_cheia(p):
    return p.topo == TAM - 1

def empilha(p, x):
    if not pilha_cheia(p):
        p.topo += 1
        p.item[p.topo] = x

def desempilha(p):
    if not pilha_vazia(p):
        x = p.item[p.topo]
        p.topo -= 1
        return x

def elemento_do_topo(p):
    if not pilha_vazia(p):
        return p.item[p.topo]

def inicializa_jogo(n):
    pilhas = [inicializa_pilha() for _ in range(n + 2)]
    return pilhas

def randomiza_jogo(pilhas, n):
    for _ in range(100):
        random.randint(0, 99)

    for i in range(n):
        for _ in range(TAM):
            x = random.randint(0, n - 1)
            while pilha_cheia(pilhas[x]):
                x = random.randint(0, n - 1)
            empilha(pilhas[x], i + 1)

def imprime_pilha(pilhas, n):
    for j in range(TAM - 1, -1, -1):
        for i in range(n):
            if pilhas[i].topo >= j:
                print(f"|{pilhas[i].item[j]}| ", end="")
            else:
                print("| | ", end="")
        print()
    
    for _ in range(n):
        print("¯¯¯ ", end="")
    print()

    for i in range(n):
        print(f" {i}  ", end="")
    print()

def manipula_pilha(pilhas, n):
    a = int(input("\n\nSelecione a Pilha que deseja desempilhar: "))
    b = int(input("Selecione a Pilha que deseja empilhar: "))
    print()
    if 0 <= a < n and 0 <= b < n and not pilha_vazia(pilhas[a]) and (elemento_do_topo(pilhas[a]) == elemento_do_topo(pilhas[b]) or pilha_vazia(pilhas[b])) and not pilha_cheia(pilhas[b]):
        x = desempilha(pilhas[a])
        empilha(pilhas[b], x)
    else:
        print("\n**Operacao INVALIDA. Tente Novamente**\n\n")

def encerra_jogo(pilhas, n):
    h = 0
    for i in range(n):
        if pilha_cheia(pilhas[i]) or pilha_vazia(pilhas[i]):
            if (pilhas[i].item[0] == pilhas[i].item[1] == pilhas[i].item[2] == pilhas[i].item[3]) or \
                    pilha_vazia(pilhas[i]):
                h += 1
            else:
                return False
        else:
            return False
    if h == n:
        print("\n============| O Jogo Terminou |============\n")
        print("              -VOCE VENCEU-               \n") 
        return True

def main():
    print("\n============| Trabalho 2 e 3 - ED |============\n")
    print("\nPor: Fernando Campideli e Natal Gaiarini\n")
    aux = 's'
    while aux == 's':
        print("\n=============================================\n")
        print("==================*INICIO*===================\n")
        n = 0
        while n < 3 or n > 7:
            n = int(input("\nDigite com quantos numeros diferentes voce quer jogar entre 3 e 7: "))
            print()
        pilhas = inicializa_jogo(n + 2)
        randomiza_jogo(pilhas, n)
        imprime_pilha(pilhas, n + 2)

        while not encerra_jogo(pilhas, n + 2):
            manipula_pilha(pilhas, n + 2)
            imprime_pilha(pilhas, n + 2)

        aux = input("\nDeseja Jogar outra vez? s/n\n")

if __name__ == "__main__":
    main()
