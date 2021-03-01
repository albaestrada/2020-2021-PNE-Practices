import Seq0

GENE_FOLDER = "./sequences/"
gene = "U5"


print("------|EXERCISE 7|------")

sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
sequence_used = []
sequence_used.append(sequence[0:20])

print("Frag:", sequence_used)
print("Comp:", Seq0.seq_complement(sequence_used))

