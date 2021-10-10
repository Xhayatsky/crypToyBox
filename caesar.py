l = list('abcdefghijklmnopqrstuvwxyz')  # mount substitution table
c = input('Write cypher text.\n>>> ')  # input cypher text from CLI
c = list(c)  # change text to character-by-character format
for i in range(len(l)):  # repeat for the number of a, b, c, ..., z
    if i < 10:
        print(' ', end='')
    print(i, ' ', end='')
    for j in range(len(c)):  # repeat for the number of cypher text
        k = i + l.index(c[j])
        if k > 25:
            k = k - 26
        d = l[k]
        print(d, end='')
    print('')