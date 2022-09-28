import spacy
import pandas as pd
import argparse, os
from recognize import recognize_pdf

os.system("python -m spacy download en_core_web_sm") # download model

NER = spacy.load("en_core_web_sm") # instantiate model

texts = []
labels = []
labels_explain = []

def extracted_ner(doc):
    for word in doc.ents:
        texts.append(word.text)
        labels.append(word.label_)
        labels_explain.append(spacy.explain(word.label_))
    df = pd.DataFrame(zip(texts, labels, labels_explain), columns=[
                      "Recognized Entities", "Entity", "Entity Meaning"])

    print(df)

    return df


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--file_path",
        help="the location where the .pdf file is saved"
    )

    args = parser.parse_args()

    file = args.file_path

    if file == None:
        print("Expected command:\npython pdf_ner.py --file_path <path to pdf>\n")

    else:
        outfilename = file.split('.')[0]+'.txt'
        if file.endswith(".pdf"):
            input_text = recognize_pdf(file)
            doc = NER(input_text)
            df = extracted_ner(doc)
            df.to_csv(outfilename, index=False)

        else:
            print(
                'Sorry, this file type is not supported. \nExpected file format is ".pdf"')

    # except:
    #     print("Expected command:\npython pdf_ner.py --file_path <path to pdf>\n")
