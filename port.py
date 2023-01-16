import sys
import json
from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Port Number", "Service Name", "Description"]

if len(sys.argv) != 2:
    print("Usage: python port.py <port_number>")
else:
    port = sys.argv[1]

    with open('spd.json') as json_file:
        found = False
        spds = json.load(json_file)

        for i in range(len(spds)):
            if str(spds[i]["0"]) == port:
                x.add_row([spds[i]["0"], spds[i]["1"], spds[i]["2"]])
    print(x)
