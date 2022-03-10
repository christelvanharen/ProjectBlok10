from Bio.Affy import CelFile

with open("GSM1019138_PA025_human_6A_070228.CEL", "rb") as handle:
    c = CelFile.read(handle)
# print(c.ncols, c.nrows)
# print(c.intensities)
print(c.DatHeader)
# print(c.AlgorithmParameters)
print(c.__dict__)