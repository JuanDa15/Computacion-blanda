import speech_recognition as sr
import time
from reportlab.pdfgen import canvas

def ConvertAUDIO(filename,name):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = r.listen(source)
        
        try:
            print("reading audio file. Please, wait a second...")
            text = r.recognize_google(audio,language="es-ES")
            time.sleep(1.5)
            print('presione 1 to create a pdf, press 2 for show in console. ')
            opcion = input()
            if(int(opcion) == 1):
                c = canvas.Canvas((name + ".pdf"))
                c.drawString(50, 50,text)
                c.save()
            if(int(opcion) == 2):
                print(text)
        except:
            print("I am sorry , cant understand")