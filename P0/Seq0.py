from pathlib import Path

def seq_ping():
    print("Ok")

def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    #a, c, g, t = 0, 0, 0, 0
    #for d in seq:
        #if d == "A":
            #a += 1
        #elif d == "C":
            #c += 1
        #elif d == "G":
            #g += 1
        #else:
            #t += 1
    #return {"A": a, "C": c, "G": g, "T": t}

    gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for d in seq:
        gene_dict[d] += 1
    return gene_dict

def seq_reverse(seq):
    inverse_seq = seq[::-1]
    return inverse_seq

def seq_complement(seq):
    comp_seq = []
    for bases in seq:
        if bases == "A":
            comp_seq.append("T")
        elif bases == "C":
            comp_seq.append(("G"))
        elif bases == "G":
            comp_seq.append("C")
        else:
            comp_seq.append("A")
    comp_seq = "".join(comp_seq)
    return comp_seq





