from Bio.Affy import CelFile
import os
from pathlib import Path

def open_zip_file():
    global path_in_str
    directory_in_str = "GSE15459_RAW"

    pathlist = Path(directory_in_str).glob('**/*.gz')
    for path in pathlist:
        path_in_str = str(path)
        # print(path_in_str)
        os.system("gunzip " + path_in_str)

def open_cel_file():
    with open("GSM387788.CEL", "rb") as handle:
        c = CelFile.read(handle)
    # print(c.ncols, c.nrows)
    # print(c.intensities)
    print(c.DatHeader)
    # print(c.AlgorithmParameters)
    print(c.__dict__)

def main():
    open_zip_file()
    open_cel_file()

main()