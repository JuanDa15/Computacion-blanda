#libraries import
import speech_recognition as sr #import library to convert audio to text
import time 
from reportlab.pdfgen import canvas #library to create pdfs
from reportlab.lib.pagesizes import letter
import numpy as np
import matplotlib.pyplot as plt
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from io import BytesIO
from scipy.io import wavfile

#Function used to convert the audio to text
def ConvertAUDIO(filename,name,array):    #Receive the filename with the extension and the name without the extension
    w,h = letter
    r = sr.Recognizer() #Initialization of the object Recognizer
    frecuencia_muestreo, senial = wavfile.read(filename)
    senial = senial / np.power(2, 15)
    senial = senial[:50]
    eje_del_tiempo = 1000 * np.arange(0, len(senial), 1) / float(frecuencia_muestreo)

    # Dibujar la señal de audio
    fig = plt.figure(figsize=(4, 3))
    plt.plot(eje_del_tiempo, senial, color='black')
    plt.xlabel('Tiempo (milisegundos)')
    plt.ylabel('Amplitud')
    plt.title('Señal Entrada de Audio')
    imgdata = BytesIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)  # rewind the data
    shape = senial.shape
    drawing=svg2rlg(imgdata)

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
                c = canvas.Canvas((name + ".pdf"), pagesize = letter) #Creation of the document name
                c.drawString((w/3),(h-50),filename)
                c.drawString(70,(h-70),("Tamaño Señal: " + str(shape)))
                c.drawString(70,(h-90),("Tipo de dato: " + array[0]))
                c.drawString(70,(h-110),("Duración señal: " + array[1]))
                c.drawString(70,(h-130),("Frecuencia de muestreo: " + array[2]))
                c.drawString(70, (h - 150),text)   #Write the audio content to pdf content
                renderPDF.draw(drawing,c, 140, 300)
                c.save()                    #Save the pdf 
            if(int(opcion) == 2):
                # Display the params
                print('\nTamaño señal:', senial.shape)
                print('Tipo de dato:', senial.dtype)
                print('Duracción de la señal:', round(senial.shape[0] / float(frecuencia_muestreo), 2), 'seconds')
                print('Frecuencia de muestreo: ', frecuencia_muestreo)

                print(text)                 #Show in console

                plt.show()
        except: #In case the audio recognizer can understant the audio
            print("I am sorry , cant understand")
    