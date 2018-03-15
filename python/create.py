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
#arg_parser.add_argument("-n",
#                        "--nomor",
#                        dest="nomor",
#                        action="store",
#                        default=None,
#                        required=True,
#                        help="Nomor Rilis")
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

nomor = re.compile=(r"<td>(\d)</td>\s*.*\s*</td>\s*.*\s*</tr>\s*<!--Posting-->")
with open("E:/an8/garismiring-an8.github.io/index.html", "r+") as nomorz:
    dataz = nomorz.read()
    nomorz.seek(0)
    fuck=re.search(nomor,dataz)
    pl0x=int(fuck.group(1))+1

html_str = """
 <tr kode="..""" + args.kode +"""" class="">
            <td>""" +str(pl0x)+"""</td>
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
