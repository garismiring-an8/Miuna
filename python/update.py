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
                        help="Inputan")

arg_parser.add_argument("-o",
                        "--output",
                        dest="output",
                        action="store",
                        default=None,
                        required=True,
                        help="Keluaran")
args = arg_parser.parse_args()
regex = re.compile=(r""+args.input+"")
with open("E:/an8/latihan1.txt", "r+") as index:
    data = index.read()
    index.seek(0)
    index.write(re.sub(regex,args.output,data))
    index.truncate()
index.close()
