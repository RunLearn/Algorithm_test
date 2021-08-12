alphabet = {'1': 1, '2': 2,'3': 3, '4': 4,'5': 5, '6': 6,'7': 7, '8': 8,'9': 9, '0': 0,
            'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,
            'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,
            'W':32,'X':33,'Y':34,'Z':35}

def RDT(X_num, X_truth):
    idx = len(str(X_num)) - 1

    if idx==0:
        return alphabet[X_num[idx]]
    return alphabet[X_num[idx]]*(X_truth ** idx) + RDT(X_num[:-1],X_truth)


print(RDT('ZZZZZ',36))