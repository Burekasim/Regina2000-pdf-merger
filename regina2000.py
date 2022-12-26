import datetime
from PyPDF2 import PdfFileMerger
import os


def get_pdf_files_from_current_folder(current_folder: str):
    output_list = []
    for item in os.listdir(current_folder):
        if item.endswith('.pdf'):
            output_list.append(item)
    return sorted(output_list)


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
