print("lets create our own audio book in phyton")
import pyttsx3 #pyton module for speech to text
import PyPDF2 #pyton module for reading an entire pdf file
book=open("basics_finmkts.pdf","rb")
pdf_reader=PyPDF2.PdfFileReader(book)
no_of_pages=pdf_reader.numPages
print(no_of_pages)

for page in range(1,no_of_pages):
    specific_page=pdf_reader.getPage(1)
    read_text=specific_page.extractText()

    speaker=pyttsx3.init()
    speaker.say(read_text)
    speaker.runAndWait()


