#---------------------------------------------------------------------------------------------
#               convert .pdf to .jpg
#---------------------------------------------------------------------------------------------
from pdf2image import convert_from_path
def pdf2jpg(folder):

    pages = convert_from_path(folder, 350, poppler_path=r"C:\Program Files\poppler-0.68.0\bin")
    folders = []
    i = 1
    for page in pages:
        str1 = '_' + '{:02d}'.format(i)
        str2 = folder.split('.')
        image_name = str2[0] + str1 + '.jpg'
        #image_name = image_name.split('.')
        page.save(image_name, "JPEG")
        #print('.....Done saving f as ' + image_name)
        i = i+1
        folders.append(image_name)
    return folders