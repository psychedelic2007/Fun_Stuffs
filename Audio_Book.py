#importing the relevant packages
import pyttsx3              #text to speech
import PyPDF2               #pdf reader

#opening the file
file = open('name_of_file.pdf','rb')
fileReader = PyPDF2.PdfFileReader(file)

#counting the number of page and printing it
pages = fileReader.numPages
print(pages)

#initialising the speaker
speaker = pyttsx3.init()

#running the for loop to read the whole file
for num in range(0, pages):
    page = fileReader.getPage(0)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()