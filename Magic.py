import os
import os.path
import sys
from os import walk
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PdfFileMerger

cwd = os.getcwd()
f = []
for (dirpath, dirnames, filenames) in walk(cwd):
    for i in filenames:
        if i.endswith('.pdf'):
            f.append(i)
print(f)
os.mkdir("Magic PDF")

merger = PdfFileMerger()

for pdf in f:
    merger.append(pdf)

merger.write("Magic PDF/Magic PDF Joiner Result.pdf")
merger.close()

""" save_path = 'Magic PDF/'
name_of_file = 'Macic Joiner Result.pdf'
completeName = os.path.join(save_path, name_of_file)       
file1 = open(completeName, "w")
file1.close() """