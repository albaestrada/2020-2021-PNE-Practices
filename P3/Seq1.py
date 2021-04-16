import termcolor
from pathlib import Path

class Seq:
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"
    VALID_BASES = ["A", "C", "G", "T"]
    """A class for representing sequences"""

    def __init__(self, strbases=NULL_SEQUENCE):
        #Initialize the sequence with the value
        #Passed as argument when creating the object

        if strbases == Seq.NULL_SEQUENCE:
            print("NULL Seq created")
            self.strbases = strbases
        else:
            self.strbases = strbases
            if self.is_valid_sequence():
                print("New sequence created!")
            else:
                self.strbases = Seq.INVALID_SEQUENCE
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
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_base(self):
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t
        else:
            for b in self.strbases:
                if b == "A":
                    a += 1
                elif b == "C":
                    c += 1
                elif b == "G":
                    g += 1
                else:
                    t += 1
            return a, c, g, t

    def count(self):
        dict_bases = {}
        for bases in Seq.VALID_BASES:
            dict_bases[bases] = self.count_base()
        return dict_bases

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            return self.strbases[::-1]

    def complement(self):
        complement = ""
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            for b in self.strbases:
                if b == "A":
                    complement += "T"
                elif b == "C":
                    complement += "G"
                elif b == "G":
                    complement += "C"
                else:
                    complement += "A"
            return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())


    def percentage(self):
        a, c, g, t = self.count_base()
        percentage_a = (a / (c + g + t)) * 100
        percentage_c = (c / (a + g + t)) * 100
        percentage_g = (g / (c + a + t)) * 100
        percentage_t = (t / (c + g + a)) * 100
        result = "\nA: " + str(a) + "(" + str(round(percentage_a, 2)) + "%" + "\nC: " + str(c) + "(" + str(round(percentage_c, 2)) + "\nG: " + str(g) + "(" + str(round(percentage_g, 2)) + "\nT: " + str(t) + "(" + str(round(percentage_t, 2))
        return result

