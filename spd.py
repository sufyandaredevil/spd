import json
import argparse
from prettytable import PrettyTable

with open("spd.json", "r") as f:
    new_data = json.load(f)

parser = argparse.ArgumentParser(description="Retrieve service name and description for a given port number. Only Well-known & Registered ports are present")
parser.add_argument("port_number", type=int, help="The port number to retrieve information for")
args = parser.parse_args()
port_number = args.port_number

if not (0 <= port_number <= 49151):
    parser.error("Invalid port number, must be between 0 and 49151")

if str(port_number) in new_data:
    table = PrettyTable()
    table.field_names = ["Port Number", "Service Name", "Description"]

    for item in new_data[str(port_number)]:
        table.add_row([port_number, item["1"], item["2"]])
    print(table)
else:
    print("{} not found. (Is that a dynamic port number?)".format(port_number))
