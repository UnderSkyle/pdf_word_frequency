from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

#init
caracter_replace = ["«" , "-" , "'", "." , "," , "<" ,">" ,"!", "?" , ":" , "»" ,";" , "…"]#add here any string you want removed from the text
word_selected = []
frequency = []
myFile = input("num du fichier et extention : ") #name of the file HAS TO BE IN THE SAME DIR

#main

#get the txt for pdf
document = PdfFileReader(open(myFile, 'rb'))
pdftext = ""
temp = range(document.numPages)
caracter_replace.extend(temp)
for page in range(document.numPages):
    pageObj = document.getPage(page)
    pdftext += pageObj.extractText().replace('\n','')
pdftext = pdftext.lower()

#clean the text of any unwanted caracter or string
for item in caracter_replace:
    pdftext = pdftext.replace(str(item), "")
list_text = pdftext.split(" ")
analyse = {}

#Simple Word counter
for word in list_text:
    if word in analyse.keys():
        analyse[word] = int(analyse.get(word))+1
    else:
        analyse[word] = 1

#sort the dict and put it into a list
for w in sorted(analyse, key=analyse.get, reverse=True):
    word_selected.append(w)
    frequency.append(analyse[w])

for k in range(int(input("Combien de mots doivent être dans la liste "))):
    print(str(word_selected[k]) + ":" + str(frequency[k]))
    


