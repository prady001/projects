from primos import eh_primo


def primos_entre(a, b):
    s = 0
    p = a
    while a <= p <= b:
        if eh_primo(p):
            s += 1
        p += 1
    return s



