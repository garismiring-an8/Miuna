#!/usr/bin/env python3
import argparse
import re
from re import *


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i",
                        "--input",
                        dest="input",
                        action="store",
                        default=None,
                        required=True,
                        help="nomor rilisan yang ingin dihapus")
args = arg_parser.parse_args()
regex4fun=(r"(<tr kode=\".*\" class=\".*\">\s*<td>"+args.input+"<.*>\s*<td class=\".*\">.*\s*<.*>\s*<td class=\"size\">.*<.*>\s*<.*>)")
with open("E:/an8/garismiring-an8.github.io/index.html", "r+") as f:
    data = f.read()
    f.seek(0)
    f.write(re.sub(regex4fun,"",data))
    f.truncate()
f.close()

pattern = re.compile(r'(<td>\d+</td>)')
pattern_digit = re.compile(r'<td>(\d+)</td>')
with open("E:/an8/garismiring-an8.github.io/index.html", "r+") as index:
    baca = index.read()
    index.seek(0)
    iterator = finditer(pattern, baca)
    count = 0
    dialog = pattern_digit.findall(baca)
    dialog1= pattern.findall(baca)
    for match in iterator:
        count +=1
    for x in range(count):
        #baca=baca.replace(str(dialog[x]),str(x+1))
        baca=baca.replace(dialog1[x], "<td>"+str(x+1)+"</td>")
    index.write(baca)
    index.truncate()
index.close()

