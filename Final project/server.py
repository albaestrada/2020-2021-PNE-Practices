import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as su
from pathlib import Path


socketserver.TCPServer.allow_reuse_address = True
PORT = 8080
ENDPOINTS = ["/listSpecies",
             "/karyotype",
             "/chromosomeLength",
             "/",
             "/geneSeq",
             "/geneInfo",
             "/geneCalc"]


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, "blue")

        url = urlparse(self.path)
        endpoint = url.path
        argument = parse_qs(url.query)
        print("Endpoint: ", endpoint)
        print("Argument: ", argument)

        GOOD_REQUEST = 200
        BAD_REQUEST = 400

        error = False
        contents = ""
        status = BAD_REQUEST

        if endpoint in ENDPOINTS:
            if endpoint == "/":
                status = GOOD_REQUEST
                contents = Path("./html/index.html").read_text()
            elif endpoint == "/listSpecies":
                if len(argument) == 0:
                    status, contents = su.list_species()
                elif len(argument) == 1:
                    try:
                        limit = int(argument['limit'][0])
                        status, contents = su.list_species(limit)
                    except (KeyError, ValueError):
                        error = True
                else:
                    error = True
            elif endpoint == "/karyotype":
                if len(argument) == 1:
                    try:
                        specie = argument['specie'][0]
                        status, contents = su.karyotype(specie)
                    except (KeyError, ValueError):
                        error = True
                else:
                    error = True
            elif endpoint == "/chromosomeLength":
                if len(argument) == 2:
                    try:
                        specie = argument['specie'][0]
                        chromo = argument['chromo'][0]
                        status, contents = su.chromosome_length(specie, chromo)
                    except (KeyError, ValueError):
                        error = True
                else:
                    error = True
            elif endpoint == "/geneSeq":
                if len(argument) == 1:
                    try:
                        gene = argument['gene'][0]
                        status, contents = su.gene_seq(gene)
                    except (KeyError, ValueError):
                        error = True
                else:
                    error = True
            elif endpoint == "/geneInfo":
                if len(argument) == 1:
                    try:
                        gene = argument['gene'][0]
                        status, contents = su.gene_info(gene)
                    except (KeyError, ValueError):
                        error = True
                else:
                    error = True
            elif endpoint == "/geneCalc":
                if len(argument) == 1:
                    try:
                        gene = argument['gene'][0]
                        status, contents = su.gene_calc(gene)
                    except (KeyError, ValueError):
                        error = True
                else:
                    error = True

        else:
            error = True

        if error:
            contents = Path("./html/error.html").read_text()

        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())


handler = TestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()