from pathlib import Path
import termcolor

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


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        #Initialize the sequence with the value
        #Passed as argument when creating the object
        self.strbases = strbases
        if self.is_valid_sequence():
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INCORRECT Sequence detected")

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = "Sequence" + str(i) + ": (Length:" + str(list_sequences[i].len()) + ")" + str(list_sequences[i])
            termcolor.cprint(text, "yellow")


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("bcbjhw")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")






