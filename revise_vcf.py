#!/usr/bin/env python
import sys

for line in sys.stdin:
    if line.startswith("##"):
        sys.stdout.write(line)
    elif line.startswith("#"):
        sys.stdout.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tHG001\n")
    else:
        row = line.strip("\n").split("\t")
        s1 = row[8]
        s2 = row[9]
        row[7] = "."
        items1 = s1.split(":")
        items2 = s2.split(":")
        if len(items1) == len(items2):
            line = "\t".join(row)
            sys.stdout.write(line + "\n")
        elif len(items1) < len(items2):
            s2 = ":".join(items2[:len(items1)])
            row[9] = s2
            line = "\t".join(row)
            sys.stdout.write(line + "\n")
        else:
            assert False
