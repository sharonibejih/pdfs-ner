# Named Entity Recognition in PDFs
Named Entity Recognition (NER) is used to retrieve textual information of entities. Examples of these entities are `names`, `location`, `date`, `organisation`, etc. It is very useful in very long texts when one needs to have a understand the context in the paper, for example in political articles, to have an idea of who or what is being discussed or in research papers, to identify the known keywords. 

Since NER is very helpful in large text data, which predominantly are in the forms of web pages or pdfs, this project is focused on the extraction of entities from PDFs documents.


## Steps taken in project:
1. Develop an OCR system for extracting texts in PDFs.
2. Apply spaCy pretrained model for named entity recognition in texts.
3. Convert the output entities to a dataframe and display the output.

## TODO:
4. Deploy the project.
5. On the app, users should be able to see the dataframe and download it as a .csv or .txt (optional).

## Run with a Linux CLI:
1. Clone this repo.

2. Create a virtual environment. 

3. Run `bash setup.sh`

## To extract entities from pdf:
4. Run `python pdf_ner.py --file_path <path/to/pdf>`. __<path/to/pdf>__ is to be replaced with the a path to a pdf file. 

## To convert pdf to text alone:
4. Run `python recognize.py --file_path <path/to/pdf>`. __<path/to/pdf>__ is to be replaced with the a path to a pdf file. 

### Output
A display of the dataframe in the terminal and a _.txt_ file containing the extracted entities.

## Major libraries:
- [pytesseract](https://github.com/madmaze/pytesseract)
- [spaCy](https://spacy.io)

