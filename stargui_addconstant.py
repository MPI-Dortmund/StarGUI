# Author: Gavin Rice
# Date 20.04.21
# Adds a column to a star file with a constant value
# Then writes a new star file from the dataframe




import os
import argparse
import starfile
import pandas as pd

parser = argparse.ArgumentParser(description='Add column with constant value')
parser.add_argument('--star', dest="filename", required=True,
                   help='Path to star file to open', metavar="FILE")
parser.add_argument('--label', type=str, required=True,
                   help='Name of the column you will add')
parser.add_argument('--value', type=str, required=True,
                   help='Value that will be applied to all rows in the new column')
args = parser.parse_args()

STAR = args.filename
NAME = args.label
VALUE = args.value

df = starfile.read(STAR)
print(df)
df[NAME] = VALUE
print(df)
starfile.new(df, 'new.star')
print("Wrote new.star in current directory.")

