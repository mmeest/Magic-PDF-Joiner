""" by Martin Maasik 2021 """
import os
import os.path
import sys
from os import walk
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

f = []                                  # Empty array for PDF files

""" cwd = os.getcwd()
for (dirpath, dirnames, filenames) in walk(cwd):    
    for i in filenames:
        if i.endswith('.pdf'):
            f.append(i)
print(f) """

for fname in os.listdir('.'):           # Iterating thru current directory
    if os.path.isdir(fname):            # If current item is folder
       pass  
    elif fname.endswith('.pdf'):        # If file name ends with '.pdf'
       f.append(fname)                  # Item will be added to to array
    else:
        pass

""" print(f) """

merger = PdfFileMerger(strict=False)    # strict=False for unindexed PDF's

for pdf in f:                           # Iterate thru created array
    merger.append(pdf)                  # PDF's will be merged together

if f.size:                              # Check if array is not empty
    os.mkdir("Magic PDF")               # Creating new folder()
    merger.write("Magic PDF/Magic PDF Joiner Result.pdf")   # Saving new file

merger.close()                          # Closing merger