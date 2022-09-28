import pytesseract
import argparse
from preprocess import pdf2img


pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

tessdata_dir_config = r'--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"'


def recognize_pdf(pdf_path):
    """Convert pdfs to images and then to text"""
    image_of_pdf = pdf2img(pdf_path)
    extractedInformation = pytesseract.image_to_string(image_of_pdf, lang="eng")

    return extractedInformation


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    try:
        parser.add_argument(
            "--file_path",
            help="the location where the .pdf file is saved"
        )

        args = parser.parse_args()

        file = args.file_path

        if file==None:
            print("Expected command:\npython recognize.py --file_path <path to pdf>\n")

        else:
            outfilename = file.split('.')[0]+'.txt'

            with open(outfilename, 'w', encoding="utf-8") as f:
                if file.endswith(".pdf"):
                    f.write(recognize_pdf(file))
                    f.close()

                else:
                    print('Sorry, this file type is not supported. \nExpected file format is ".pdf"')
                    f.close()

    except:
        print("Expected command:\npython recognize.py --file_path <path to pdf>\n")

    
            
