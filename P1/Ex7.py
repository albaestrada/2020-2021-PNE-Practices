from Seq1 import Seq

def print_count_bases(sequence):
    for base in Seq.VALID_BASES:
        print(f"{base}: {sequence.count_base(base)}  ", end="")
        print("Rev: ", sequence.reverse())
    print()

print("----- Exercise 7 ------")


from Seq1 import Seq


print("----- | Exercise 7 | ------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid Sequence")

print(f"Sequence 0: (Length: {s1.len()}) {s1}")
print(f"Bases: {s1.count()}")
print(f"Rev: {s1.reverse()}")
print(f"Sequence 1: (Length: {s2.len()}) {s2}")
print(f"Bases: {s2.count()}")
print(f"Rev: {s2.reverse()}")
print(f"Sequence 2: (Length: {s3.len()}) {s3}")
print(f"Bases: {s3.count()}")
print(f"Rev: {s3.reverse()}")