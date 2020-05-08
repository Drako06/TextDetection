from PIL import Image
import os
from Utility import conn
import pytesseract
import PyPDF2
from tabula import read_pdf
import pandas as pd
from pdf2image import convert_from_path, convert_from_bytes
pytesseract.pytesseract.tesseract_cmd = conn.pathPytesseract
#print(pytesseract.image_to_string(Image.open('Captura.PNG')))#, lang='spa'))
# #
pdf_path = conn.path
#
# pages = convert_from_path(pdf)
# contador = 1
# # for page in pages:
# filename = "page_" + str(contador) + ".PNG"
# pages.save(pdf, 'PNG')
# #     contador += 1
# # limit = contador-1
# print('asdasdadas')
# #for i in range(1, limit+1):
# filename = "page_" + str(filename) + ".PNG"
# text = str(((pytesseract.image_to_string(Image.open(filename)))))
# text = text = text.replace('-\n', '')
# print(text)
# print("salimos")
# # doc = open(pdf)
# # read = PyPDF2.PdfFileReader(doc)
# # #number_pages = read.getNumPages()
# # #print(number_pages)
# # page = read.getPage(0)
# # text = page.extractText()
# # print(text)
#
# #images = convert_from_bytes(open('/home/belval/example.pdf', 'rb').read())

with open('Ticket.pdf','rb') as pdfFIle:  #'rb' for read binary mode
    pdfReader = PyPDF2.PdfFileReader(pdfFIle)
    #pdfReader.numPages
    pageObj = pdfReader.getPage(0)
    print(pageObj)
    text = pageObj.extractText()
    #text.encode('utf-8')  # '9' is the page number
    print('Imprime texto del pdf')
    print(text)
    """
    convierte el pdf a imagen dependiendo la pagina"""
    #image_from_path = convert_from_path(pdf_path, poppler_path='C:/poppler-0.68.0/bin/')
    #for page in image_from_path:
    #    filename = "page_1.PNG"
    #    page.save(filename, 'PNG')
    """
    extrae texto de la imagen convertida de pdf"""
    filename = "page_1.PNG"
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text = text.replace('-\n', '')
    print('Imprime el texto del pdf convertido a imagen')
    print(len(text))
    print(text)
    print("salimos")



"""Extrae tablas de un pdf y convierte a dataset"""
pdf = read_pdf("alcanza.png")
print(len(pdf))

data = pd.DataFrame(pdf[0])
print(data)
