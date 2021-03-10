from Seq1 import Seq

def print_count_bases(sequence):
    for base in Seq.VALID_BASES:
        print(f"{base}: {sequence.count_base(base)}  ", end="")
    print()


print("----- | Exercise 5 | ------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid Sequence")

print(f"Sequence 0: (Length: {s1.len()}) {s1}")
print_count_bases(s1)
print(f"Sequence 1: (Length: {s2.len()}) {s2}")
print_count_bases(s2)
print(f"Sequence 2: (Length: {s3.len()}) {s3}")
print_count_bases(s3)





