from Seq1 import Seq
import pathlib
import jinja2
import http.client
import json
from pathlib import Path


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
    result = "\nTotal length: " + str(seq.len()) + seq.percentage()
    context = {
        "sequence": seq,
        "operation": info,
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


SERVER = 'rest.ensembl.org'
GOOD_REQUEST = 200
BAD_REQUEST = 400


def list_species(limit=None):
    endpoint = '/info/species'
    argument = '?content-type=application/json'
    url = endpoint + argument

    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", url)
    response = connection.getresponse()
    status = GOOD_REQUEST
    if response.status == GOOD_REQUEST:
        data = json.loads(response.read().decode("utf-8"))
        try:
            species = data['species']
            context = {
                "total": len(species),
                "species": species[:limit],
                "limit": limit
            }
            contents = read_template_html_file("./html/species.html").render(context=context)
        except KeyError:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


def karyotype(specie):
    endpoint = '/info/assembly/'
    argument = f'{specie}?content-type=application/json'
    url = endpoint + argument

    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", url)
    response = connection.getresponse()
    status = GOOD_REQUEST
    if response.status == GOOD_REQUEST:
        data = json.loads(response.read().decode("utf-8"))
        try:
            karyotype = data['karyotype']

            context = {
                "karyotype": karyotype,
            }
            contents = read_template_html_file("./html/karyotype.html").render(context=context)
        except KeyError:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


def chromosome_length(specie, chromo):
    endpoint = '/info/assembly/'
    parameters = f'{specie}?content-type=application/json'
    url = endpoint + parameters

    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", url)
    response = connection.getresponse()
    status = GOOD_REQUEST
    if response.status == GOOD_REQUEST:
        data = json.loads(response.read().decode("utf-8"))
        try:
            key = data['top_level_region']
            length = 0
            for chromosome in key:
                if chromosome['name'] == chromo:
                    length = chromosome['length']
                    break

            context = {
                "length": length,
            }
            contents = read_template_html_file("./html/chromosomeLength.html").render(context=context)
        except KeyError:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


DICT_GENES = {
    "FRAT1": "ENSMUSG00000067199",
    "ADA": "ENSG00000196839",
    "FXN": "ENSMUSG00000059363",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000226906",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSMUSG00000062960",
    "ANK2": "ENSG00000145362"
}
def error(gene):
    if gene in DICT_GENES:
        no_error = True
        id = DICT_GENES[gene]
    else:
        no_error = False
        id = ""
    return no_error, id

def connection(url):
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", url)
    response = connection.getresponse()
    status = GOOD_REQUEST
    return response, status

def gene_seq(gene):
    no_error = error(gene)[0]
    id = error(gene)[1]
    if no_error:
        endpoint = '/sequence/id/'
        argument = '?content-type=application/json'
        url = endpoint + id + argument
        response = connection(url)[0]
        status = connection(url)[1]

        if response.status == GOOD_REQUEST:
            data = json.loads(response.read().decode("utf-8"))
            try:
                bases = data['seq']

                context = {
                    "gene": gene,
                    "bases": bases
                }
                contents = read_template_html_file("html/geneSeq.html").render(context=context)
            except KeyError:
                status = BAD_REQUEST
                contents = Path("./html/error.html").read_text()
        else:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()

    return status, contents


def gene_info(gene):
    no_error = error(gene)[0]
    id = error(gene)[1]

    if no_error:
        endpoint = '/sequence/id/'
        argument = '?feature=gene;content-type=application/json'
        url = endpoint + id + argument
        response = connection(url)[0]
        status = connection(url)[1]

        if response.status == GOOD_REQUEST:
            data = json.loads(response.read().decode("utf-8"))
            try:
                data2 = data['desc']
                data2 = data2.split(":")
                data2 = list(data2)
                start = int(data2[3])
                end = int(data2[4])
                length = end - start
                chromosome_name = data2[2]
                context = {
                    "gene": gene,
                    "start": start,
                    "end": end,
                    "id": id,
                    "length": length,
                    "chromosome_name": chromosome_name
                }
                contents = read_template_html_file("html/geneInfo.html").render(context=context)
            except (KeyError, IndexError):
                status = BAD_REQUEST
                contents = Path("./html/error.html").read_text()
        else:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


def gene_calc(gene):
    no_error = error(gene)[0]
    id = error(gene)[1]

    if no_error:
        endpoint = '/sequence/id/'
        argument = '?content-type=application/json'
        url = endpoint + id + argument
        response = connection(url)[0]
        status = connection(url)[1]
        
        if response.status == GOOD_REQUEST:
            data = json.loads(response.read().decode("utf-8"))
            try:
                bases = data['seq']
                seq = Seq(bases)
                context = {
                    "gene": gene,
                    "seq": seq
                }
                contents = read_template_html_file("html/geneCalc.html").render(context=context)
            except KeyError:
                status = BAD_REQUEST
                contents = Path("./html/error.html").read_text()
        else:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents
