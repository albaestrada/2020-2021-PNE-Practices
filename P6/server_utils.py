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



def info(sequence):
    seq = Seq(sequence)
    result = Seq.len(seq)
    for base, count in seq.count().items():
        result += f"{base}: {count} ({seq.percentage(base)}%)<br><br>"
    context = {
        "sequence": seq,
        "operation": "info",
        "result": result
    }

    contents = read_template_html_file("./html/operate.html").render(context=context)
    return contents


def comp(sequence):
    seq = Seq(sequence)
    context = {
        "sequence": seq,
        "operation": "comp",
        "result": seq.complement()
    }

    contents = read_template_html_file("./html/operate.html").render(context=context)
    return contents

def rev(sequence):
    seq = Seq(sequence)
    context = {
        "sequence": seq,
        "operation": "rev",
        "result": seq.reverse()
    }

    contents = read_template_html_file("./html/operate.html").render(context=context)
    return contents


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








