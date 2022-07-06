# Author: Gavin Rice
# Date 20.04.21
# Adds two columns together replacing the values from the first column with the sum
# Then writes a new star file from the dataframe




import os
import argparse
import starfile
import pandas as pd

#arguments for CLI
parser = argparse.ArgumentParser(description='Adds two columns together replacing the values from the first column with the sum')
parser.add_argument('--star', dest="filename", required=True,
                   help='Path to star file to open', metavar="FILE")
parser.add_argument('--ColumnA', type=str, required=True,
                   help='Name of the column you will add TO')
parser.add_argument('--ColumnB', type=str, required=True,
                   help='Name of the column you will add FROM')
args = parser.parse_args()

STAR = args.filename
ColumnA = args.ColumnA
ColumnB = args.ColumnB

#Data manipulation
df = starfile.read(STAR)
print(df)
df[ColumnA] = df[ColumnA] + df[ColumnB]
print(df)
starfile.new(df, 'new.star')
print("Wrote new.star in current directory.")

