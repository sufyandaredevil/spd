import sys
import json
from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Port Number", "Service Name", "Description"]

if len(sys.argv) != 2:
    print("Usage: python spd.py <port_number>")
else:
    port = sys.argv[1]
    mark = None

    with open('spd.json') as json_file:
        spds = json.load(json_file)

        for i in range(len(spds)):
            if mark != None and spds[i]["0"] > mark:
                print(x)
                break
            if str(spds[i]["0"]) == port:
                x.add_row([spds[i]["0"], spds[i]["1"], spds[i]["2"]])
                mark = int(port)

    if mark == None:
        print('No service names found for ', port)
