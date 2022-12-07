import requests
import sys
import base64
import zlib
import argparse

## generate a args parser
parser = argparse.ArgumentParser()

parser.add_argument('--filepath', type=str, default='../source/hello.dot')
parser.add_argument('--svgtype', type=str, default='graphviz')
args = parser.parse_args()

file_path = args.filepath
svgtype = args.svgtype

## read file data
data = open(file_path, encoding="utf-8")
file_data = data.read()
data.close()

## encoding data
encoding = base64.urlsafe_b64encode(zlib.compress(file_data.encode('utf-8'), 9)).decode('ascii')
server_url = "http://127.0.0.1:8000/" + svgtype + "/svg/" + encoding

# print(server_url)
res = requests.get(url=server_url)
output_file = open("../output/" + args.svgtype + "_temp.svg", "w")
output_file.write(res.text)

