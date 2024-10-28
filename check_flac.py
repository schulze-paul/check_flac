import subprocess
import os
from tqdm import tqdm

mypath = "/home/paul/Music/LOSSLESS"

f = [os.path.join(dirpath, f) for (dirpath, dirnames, filenames)
     in os.walk(mypath) for f in filenames]

errors = []

for filename in tqdm(f):
    if filename[-5:] == ".flac":
        process = subprocess.run(
            ["flac", "-t", filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if process.returncode != 0:
            errors.append(filename)
            print(filename)


for filename in tqdm(errors):
    process = subprocess.run(
        ["flac", "-t", filename])
