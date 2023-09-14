import datetime
from PyPDF2 import PdfFileMerger
import os
import re


def natural_sort(l):
    # use natural sort instead of sorted, taken from https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def get_pdf_files_from_current_folder(current_folder: str):
    output_list = []
    for item in os.listdir(current_folder):
        if item.endswith('.pdf'):
            output_list.append(item)
    return natural_sort(output_list)


if __name__ == '__main__':
    folder = os.getcwd()
    pdfs = get_pdf_files_from_current_folder(folder)
    os.chdir(folder)

    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)

    current_time = datetime.datetime.now().strftime('%H%M%S')

    merger.write(f'{current_time}-regina2000.pdf')
    merger.close()
