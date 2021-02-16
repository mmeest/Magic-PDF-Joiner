<p align="center">
<img src="magic.ico" width="60" height="60">
</p>

# Magic-PDF-Joiner
Program for joining all PDF's in current directory

## Features
* Doubleclick on 'Magic PDF Joiner.exe'
* All PDF's in current directory will be joined
* And saved in 'Magic PDF/Magic PDF Joiner Result.pdf'

# Version history:

## V.2021.02.16
* Ignoring directories in working folder
* If no PDF's in working directory, then nothing will be written

## V.2021.02.15
* Removed 'xref table not zero-indexed' error by adding strict=False
```
merger = PdfFileMerger(strict=False)
```

## V.2021.02.12
* Initial version

## To create executable with heart icon('magic.ico'):
* pip install pyinstaller
* pyinstaller -F -i "magic.ico" --version-file=.\version.rc Magic.py
