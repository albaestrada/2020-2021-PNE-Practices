import Seq0

GENE_FOLDER = "./sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("------|EXERCISE 5|------")


cont_a = 0
cont_t = 0
cont_c = 0
cont_g = 0

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    for bases in sequence:
        if bases == "A":
            cont_a += 1
        elif bases == "T":
            cont_t += 1
        elif bases == "C":
            cont_c += 1
        else:
            cont_g += 1

    if cont_a > cont_g and cont_a > cont_t and cont_a > cont_c:
        maximum = "A"
    elif cont_c > cont_g and cont_c > cont_t and cont_c > cont_a:
        maximum = "C"
    elif cont_t > cont_g and cont_t > cont_a and cont_t > cont_c:
        maximum = "T"
    else:
        maximum = "G"

    print("Gene", gene, ":", maximum)

