import Seq0

GENE_FOLDER = "./sequences/"
gene = "U5"


print("------|EXERCISE 6|------")

sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
sequence_used = sequence[0:20]

print("Gene U5:")
print("Frag:", sequence_used)
print("Rev:", Seq0.seq_reverse(sequence_used))


