import termcolor

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        #Initialize the sequence with the value
        #Passed as argument when creating the object

        if strbases == "NULL":
            print("NULL Seq created")
            self.strbases = strbases
        else:
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
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return self.strbases.count(base)

    def count(self):
        dict_bases = {}
        for bases in ["A", "C", "G", "T"]:
            dict_bases[bases] = self.count_base(bases)
        return dict_bases
