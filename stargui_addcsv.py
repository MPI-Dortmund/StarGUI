# Author: Gavin Rice
# Date 20.04.21
# Adds a column to a star file with values from a CSV file
# Then writes a new star file from the dataframe
# Starfile: github.com/alisterburt/starfile

import os
import argparse
import starfile
import pandas as pd

parser = argparse.ArgumentParser(description='Adds a column to a star file with values from a CSV file')
parser.add_argument('--star', dest="filename", required=True,
                   help='Path to star file to open', metavar="FILE")
parser.add_argument('--label', type=str, required=True,
                   help='Name of the column you will add')
parser.add_argument('--csv', dest="filename", required=True,
                   help='Path to CSV containing values for new column', metavar="FILE")
args = parser.parse_args()

STAR = args.filename
NAME = args.label
VALUES = args.filename

df1 = starfile.open(STAR)
print(df1)
df2 = pd.read_csv(VALUES)
result = pd.concat([df1,df2], axis=1)
print(result)
starfile.new(result, 'new.star')
print("Wrote new.star in current directory.")


