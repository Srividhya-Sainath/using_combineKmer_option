## Step 1: Unzip gzip file
## Step 2: Replacing operation
## Step 3: Zip the file again

import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser(description="Converting the output of DSK, into pyseer appropriate input")
parser.add_argument('-f','--file', help="Provide the .gz output file of DSK run")
args = parser.parse_args()

f = open(args.file,"r")
fileName = os.path.basename(f.name)
print("Unzipping the file", fileName)
subprocess.run(["gunzip",fileName])

### Removing .gz from the string fileName
fileName = fileName[:-3]

print("File unzipped. Starting the convertion")

subprocess.run(["sed","-i", "s/C GCG/C | GCF/g",fileName])
subprocess.run(["sed","-i", "s/G GCG/G | GCF/g",fileName])
subprocess.run(["sed","-i", "s/T GCG/T | GCF/g",fileName])

print("Almost there !")

subprocess.run(["sed","-i", "s/A GCG/A | GCF/g",fileName])
subprocess.run(["gzip",fileName])

print("Completed")
