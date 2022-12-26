# Regina2000: Easy PDF merger tool

A simple executible (.exe) to merge PDF files

**Why?**

I created this tool because my roommate [kept asking me](https://www.linkedin.com/posts/avi-keinan-14828738_my-room-mate-regina-kogan-started-a-new-activity-6963108087318626304-TvgK/) to merge PDF files for her, 
I didn't want to use shady websites with no privacy policy and my internet upload speed is not fast enough so I created this tool for Windows users. 

**How does it work?**

Collect all the PDF files you would like to merge in a folder with regina2000.exe file, run regina2000.exe and a new PDF file will be created.

**Can I control the order of the files?**

Yes, The files are arranged in alphabetical order. 

If you want to control the order of the files, you can add a number at the beginning of each file.

 For example: if we have three files:

demo.pdf
executive.pdf
example.pdf

If I rename example.pdf to **0**example.pdf. It will be the first file in the output file.

**What is the output file name format?**

The output file name will be HHMMSS-regina2000.pdf. 

For exapmle, if I run regina2000.exe exactly at 12PM, the file name would be: 120000-regina2000.py

**Does the software collect sensitive information?**

No. it just merge all the pdf files in the directory to a single PDF file.

**How do I compile the python file into a executible?**

Using [pyinstaller](https://www.pyinstaller.org/ "pyinstaller") library, you can build the exe by running:

`pyinstaller.exe --onefile --windowed regina2000.py`
