# Author: Gavin Rice
# Date 03.05.21
# Adds columns from one star file to another



import os
import argparse
import starfile
import pandas as pd

#arguments for CLI
parser = argparse.ArgumentParser(description='Add column from star2 to star')
parser.add_argument('--star', dest="filename", required=True,
                   help='Path to star file to add to', metavar="FILE")
parser.add_argument('--star2', dest="filename2", required=True,
                   help='Path to star file to add from', metavar="FILE")
parser.add_argument('--column', type=str, required=True,
                   help='Column to add')
args = parser.parse_args()

STAR = args.filename
STAR2 = args.filename2
col = args.column


# Data manipulation
df = starfile.read(STAR)
print(df)
df2 = starfile.read(STAR2)
df[col] = df2[col]


print(df)

starfile.new(df, 'new.star')
print("Wrote new.star in current directory.")

