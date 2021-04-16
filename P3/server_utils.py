import termcolor
from Seq1 import Seq

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping(cs):
    print_colored("PING command", "green")
    response = "OK"
    cs.send(response.encode())
    cs.close()


def get(cs, n, SEQUENCES_LIST):
    termcolor.cprint("GET", "green")
    seq = SEQUENCES_LIST[n]
    termcolor.cprint(f"{seq}\n", 'white')
    cs.send(f"{seq}".encode())
    cs.close()

def info(cs, seq):
    termcolor.cprint("INFO", "green")
    seq = Seq(seq)
    len_seq = Seq.len(seq)
    count_seq = Seq.count(seq)
    termcolor.cprint(f"{len_seq}, {count_seq}", 'white')
    cs.send(f"{len_seq}, {count_seq}".encode())
    cs.close()

def comp(cs, seq):
    termcolor.cprint("COMP", "green")
    seq = Seq(seq)
    complement = Seq.complement(seq)
    termcolor.cprint(complement, "white")
    cs.send(complement.encode())
    cs.close()

def rev(cs,seq):
    termcolor.cprint("REV", "green")
    seq = Seq(seq)
    reverse = Seq.reverse(seq)
    termcolor.cprint(reverse, "white")
    cs.send(reverse.encode())
    cs.close()


def gene(cs, filename):
    termcolor.cprint("GENE", "green")
    seq = Seq()
    seq.read_fasta(filename)
    termcolor.cprint(seq, "white")
    cs.send(f"{seq}\n".encode())
    cs.close()








