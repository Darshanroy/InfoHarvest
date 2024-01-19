import docx2txt as docx2txt
import fitz
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import sys


class TextExtractor:
    def __init__(self):
        pass
    #
    def extract_text_from_docx(self, docx_path):
        try:
            text = docx2txt.process(docx_path)
            return text
        except Exception as e:
            return docx_path


    def extract_text_from_pdf(self, pdf_path):
        text = ""
        pdf_document = fitz.open(pdf_path)
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
        pdf_document.close()
        return text

    def rename_doc_to_docx(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".doc"):
                new_filename = os.path.splitext(filename)[0] + ".docx"
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

    def extract_file_names(self, directory_path):
        self.rename_doc_to_docx(directory_path)
        file_names = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_names.append(file)
        return file_names

class ResumeTextExtractor(TextExtractor):
    def __init__(self):
        super().__init__()

    def extract_text_from_resumes(self, folder_path='uploads/'):
        # file_names = self.extract_file_names(folder_path)
        concatenated_text = ""
        # corrupted_files = []

        try:
            #     for file_name in file_names:
            if folder_path.endswith('.pdf'):
                text = self.extract_text_from_pdf(folder_path)
                concatenated_text += text + "\n\n"
            elif folder_path.endswith('.docx'):
                text = self.extract_text_from_docx(folder_path)
                # if text == folder_path + file_name:
                #     corrupted_files.append(text)
                # else:
                concatenated_text += text 

            return concatenated_text

        except Exception as e:
            return None, []
