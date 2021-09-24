import pdfplumber
import pyttsx3


pdf_file = ''## Add pdf file path here ##
engine = pyttsx3.init()

def pdf_to_voice(file):
#Open pdf
    with pdfplumber.open(file) as pdf:
        book = ''
        #Get total pages
        total_pages = len(pdf.pages)
        #loop through pages
        for i in range(0, total_pages-1):
            #Extract text
            page = pdf.pages[i].extract_text()
            book = book + page
        #Save to file
        engine.save_to_file(book, 'book.mp3')
        engine.runAndWait()


pdf_to_voice(pdf_file)
