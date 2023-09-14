l1 = []
k = True
while k:
    n = int(input('Digite um número: '))
    if n > 0:
        l1.append(n)
    else:
        l1.append(n)
        k = False

i = len(l1)
x = len(l1) - 1
l2 = []
while i > 0:
    l2.append(l1[x])
    i -= 1
    x -= 1
l1 = l2

j = 0
while j < len(l1):
    print(l1[j])
    j += 1