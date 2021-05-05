import http.client
import json

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

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
ID = DICT_GENES["MIR633"]
PARAMETERS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + ID + PARAMETERS)
response = connection.getresponse()
print("Response receive!: ", response.status, response.reason)
if response.status == 200:
    response = json.loads(response.read().decode())
    print(json.dumps(response, indent=4, sort_keys=True))
    print("Gene:", ID)
    print("Description:", response["desc"])
    print("Bases:", response["seq"])
elif response.status == 404:
    print("Check if the ENDPOINT was correctly written!!!!!!!!!!!!!!!!!!!!!")


