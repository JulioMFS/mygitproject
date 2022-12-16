from PIL import Image
from pytesseract import pytesseract
def getJpg(folder):

    path_to_tesseract = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    # Opening the image & storing it in an image object
    img = Image.open(folder)

    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)
    # Displaying the extracted text
    txt = text[:-1].split('\n')
    #print(type(txt))
    #for t in txt:
    #    print(t)
    #print(text[:-1])
    return txt
