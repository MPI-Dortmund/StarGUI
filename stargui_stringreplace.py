# Author: Gavin Rice
# Date 03.05.21
# Changes the names of all files in a column using a string match



import os
import argparse
import starfile
import pandas as pd

#arguments for CLI
parser = argparse.ArgumentParser(description='Changes the names of all files in a column using a string match')
parser.add_argument('--star', dest="filename", required=True,
                   help='Path to star file to open', metavar="FILE")
parser.add_argument('--Column', type=str, required=True,
                   help='Column name where your string is')
parser.add_argument('--Current', type=str, required=True,
                   help='text string you want to remove')
parser.add_argument('--Replacement', type=str, required=False, default=None,
                   help='text string to replace it with (ignore this if you just want to delete something)')
args = parser.parse_args()

STAR = args.filename
col = args.Column
cur = args.Current
rep = args.Replacement

# Data manipulation
df = starfile.open(STAR)
print(df[col])

if rep == None :
    df[col] = df[col].str.replace(cur,'')
else :
    df[col] = df[col].str.replace(cur,rep)

print(df[col])


starfile.new(df, 'new.star')
print("Wrote new.star in current directory.")

