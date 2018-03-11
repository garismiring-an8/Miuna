#!/usr/bin/env python3
import argparse
import re

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i",
                        "--input",
                        dest="input",
                        action="store",
                        default=None,
                        required=True,
                        help="nomor rilisan yang ingin dihapus")
args = arg_parser.parse_args()
regex4fun=(r"(<tr kode=\".*\" class=\".*\">\s*<td>"+args.input+"<.*>\s*<td class=\".*\">.*\s*<.*>\s*<td class=\"size\">\d+<.*>\s*<.*>)")
with open("E:/an8/garismiring-an8.github.io/index.html", "r+") as index:
    data = index.read()
    index.seek(0)
    index.write(re.sub(regex4fun,"",data))
    index.truncate()
index.close()
