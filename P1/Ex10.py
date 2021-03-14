from Seq1 import Seq

print("----- | Exercise 10 | ------")

GENES = ["ADA.txt", "FRAT1.txt", "FXN.txt", "RNU6_269P.txt", "U5.txt"]

count_a = 0
count_c = 0
count_g = 0
count_t = 0

for i in GENES:
    seq = Seq()
    for base in i:
        if base == "A":
            count_a += 1
        elif base == "C":
            count_c += 1
        elif base == "G":
            count_g += 1
        else:
            count_t += 1
    if count_a > count_c and count_a > count_g and count_a > count_t:
        print("Gene", i, ": Most frequent base: A")
    elif count_c > count_a and count_c > count_g and count_c > count_t:
        print("Gene", i, ": Most frequent base: C")
    elif count_g > count_a and count_g > count_c and count_g > count_t:
        print("Gene", i, ": Most frequent base: G")
    else:
        print("Gene", i, ": Most frequent base: T")
