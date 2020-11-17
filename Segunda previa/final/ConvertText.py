#libraries import
import speech_recognition as sr #import library to convert audio to text
import time 
from reportlab.pdfgen import canvas #library to create pdfs

#Function used to convert the audio to text
def ConvertAUDIO(filename,name):    #Receive the filename with the extension and the name without the extension
    r = sr.Recognizer() #Initialization of the object Recognizer

    with sr.AudioFile(filename) as source: #Open the file to convert the audio
        audio = r.listen(source)    #The recognizer heard the audio
        
        try:    #We use the try in case the audio has nothing to convert
            print("reading audio file. Please, wait a second...")
            text = r.recognize_google(audio,language="es-ES") #We use the google recognition to convert
            time.sleep(1.5)
            print('presione 1 to create a pdf, press 2 for show in console. ')
            opcion = input()
            #Pdf creation or answer in console 
            if(int(opcion) == 1):
                c = canvas.Canvas((name + ".pdf")) #Creation of the document name
                c.drawString(50, 50,text)   #Write the audio content to pdf content
                c.save()                    #Save the pdf 
            if(int(opcion) == 2):
                print(text)                 #Show in console
        except: #In case the audio recognizer can understant the audio
            print("I am sorry , cant understand")