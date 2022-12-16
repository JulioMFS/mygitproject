#---------------------------------------------------------------------------------------------
#               Print .pdf file
#---------------------------------------------------------------------------------------------
# importing required modules
import PyPDF2

def getPdf(folder):
    # creating a pdf file object
    pdfFileObj = open(folder, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    #print(pdfReader.numPages)
    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    txt = pageObj.extractText().split('\n')
    #print(type(txt), len(txt))

    # closing the pdf file object
    pdfFileObj.close()
    return txt
