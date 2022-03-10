from Bio.Affy import CelFile

with open("GSM387788.CEL", "rb") as handle:
    c = CelFile.read(handle)
# print(c.ncols, c.nrows)
# print(c.intensities)
print(c.DatHeader)
# print(c.AlgorithmParameters)
print(c.__dict__)