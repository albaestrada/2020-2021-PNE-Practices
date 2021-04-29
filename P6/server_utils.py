import termcolor
from Seq1 import Seq
import pathlib
import jinja2

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def ping(cs):
    print_colored("PING command", "yellow")
    response = "OK"
    cs.send(response.encode())
    cs.close()


def get(n, SEQUENCES_LIST):
    sequence = SEQUENCES_LIST[int(n)]
    context = {
        "number": n,
        "sequence": sequence,
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents



def info(cs, seq):
    termcolor.cprint("INFO", "yellow")
    seq = Seq(seq)
    len_seq = Seq.len(seq)
    count_seq = Seq.count(seq)

    response = "Sequence: " + str(seq) + "\nTotal length: " + str(len_seq) + seq.percentage()
    print(response)
    cs.send(response.encode())
    cs.close()

def comp(cs, seq):
    termcolor.cprint("COMP", "yellow")
    seq = Seq(seq)
    complement = Seq.complement(seq)
    termcolor.cprint(complement, "white")
    cs.send(complement.encode())
    cs.close()

def rev(cs,seq):
    termcolor.cprint("REV", "yellow")
    seq = Seq(seq)
    reverse = Seq.reverse(seq)
    termcolor.cprint(reverse, "white")
    cs.send(reverse.encode())
    cs.close()


def gene(seq_name):
    PATH = "./sequences/" + seq_name + ".txt"
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {
        "gene_name": seq_name,
        "gene_contents": s1.strbases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents








