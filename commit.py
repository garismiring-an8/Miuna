#!/usr/bin/env python3
import argparse
import re

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-k",
                        "--kode",
                        dest="kode",
                        action="store",
                        default=None,
                        required=True,
                        help="Kode Google Drive")
arg_parser.add_argument("-n",
                        "--nomor",
                        dest="nomor",
                        action="store",
                        default=None,
                        required=True,
                        help="Nomor Rilis")
arg_parser.add_argument("-r",
                        "--rilisan",
                        dest="rilisan",
                        action="store",
                        default=None,
                        required=True,
                        help="Nama Rilisan")
arg_parser.add_argument("-u",
                        "--ukuran",
                        dest="ukuran",
                        action="store",
                        default=None,
                        required=True,
                        help="Ukuran Rilisan")
args = arg_parser.parse_args()

html_str = """
 <tr kode="..""" + args.kode +"""" class="">
            <td>"""+ args.nomor +"""</td>
            <td class="name">""" + args.rilisan +"""
</td>
            <td class="size">"""+ args.ukuran +"""</td>
        </tr>
    <!--Posting-->

"""

regex = re.compile=(r"<!--Posting-->")
with open("E:/an8/garismiring-an8.github.io/index.html", "r+") as index:
    data = index.read()
    index.seek(0)
    index.write(re.sub(r"<!--Posting-->",html_str,data))
    index.truncate()
index.close()
