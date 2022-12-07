def primos_entre_si(x, y):
    """Verifica se x e y são primos entre si"""
    for c in range(2, y+1):
        if (x % c == 0) and (y % c == 0):
            return False

    return True


def definir_base():

    base = (B-1)**2 + (B-1) * (A-B)
    X3 = Y3 = 0

    while True:
        resultado = X3*B + Y3*A

        if (base > resultado):
            Y3 = X3+1
            X3 = 0
        elif (base < resultado):
            X3 = Y3+1

        else:
            break

    print(f"A proposição é verdadeira a partir de {base} centavos.")
    print(f"O valor {base} centavos pode ser feito usando {X3} selo(s) de {A} centavos e {Y3} selo(s) de {B} centavos.")


def definir_passos():
    """Função para definir os padrões"""
    X1 = Y1 = 1
    checkpoint_y1 = 1

    global A, B

    while True:
        # Determinar a Primeira Operação
        resultado = X1*A - Y1*B
        if (X1*A > Y1*B):
            # Verifica se o resultado é positivo, se sim, incrementa Y1
            Y1 = Y1 + 1
            checkpoint_y1 = Y1
        elif resultado == - 1:
            break
        elif (X1*A < Y1*B):
            # Verifica se é negativo, como o resultado é negativo e != 1, Y1 = 1 e incrementa X1
            X1 = X1 + 1
            Y1 = checkpoint_y1

    X2 = Y2 = 1
    checkpoint_y2 = 1
    while True:
        # Determinar a Segunda Operação
        resultado = X2*B - Y2*A
        if (X2*B > Y2*A):
            # Verifica se o resultado é positivo, se sim, incrementa Y2
            Y2 = Y2 + 1
            checkpoint_y1 = Y2
        elif resultado == - 1:
            break
        elif (X2*B < Y2*A):
            # Verifica se é negativo, como o resultado é negativo e != 1, Y1 = 1 e incrementa X1
            X2 = X2 + 1
            Y2 = checkpoint_y2

    if X1 > X2:
        # Garante que os passos mais simples serão apresentados primeiro
        aux_x = X1
        aux_y = Y1
        aux = A
        X1 = X2
        Y1 = Y2
        X2 = aux_x
        Y2 = aux_y
        A = B
        B = aux

    print(f"[III] Troque {X1} selo(s) de {A} centavos por {Y1} selo(s) de {B} centavos ou Troque {X2} selo(s) de {B} centavos por {Y2} selo(s) de {A} centavos.\n")


def ler_valores():
    """Função responsável por ler os valores e organiza-los"""
    global A, B
    A = int(input("Digite o Primeiro Valor: "))
    B = int(input("Digite o Segundo Valor: "))

    if B > A:
        # Garante que o maior valor sempre vai estar em A (Facilita na implementação)
        aux = A
        A = B
        B = aux

    if (A == 0) or (B == 0):
        # Garante que nenhum selo seja igual a 0
        print("[!] Não existe selos de 0 centavos!\n")
        return False
    elif not primos_entre_si(A, B):
        print(
            "[!] A e B devem ser primos entre sí!\n")
        return False
    elif B == A:
        # Garante que A é diferente de B
        print("[!] Os valores de A e B são iguais, insira valores diferentes!\n")
        return False
    elif (A == 1) or (B == 1):
        # Garante que nenhum numero é igual a 1
        print("[!] Você pode representar valores usando o Selo de 1!\n")
        return False
    else:
       # Todos os valores estão corretos e não há erros
        return True


while True:

    if ler_valores():
        # definir_base()
        definir_passos()
    else:
        break
