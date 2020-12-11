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
def ConvertAUDIO(filename,name,array):    # Recibe el nombre del archivo con extencion, nomrbe sin extension y arreglo
    w,h = letter    #Se extraen las dimensiones de una hoja tamaño carta

    r = sr.Recognizer() #Inicializacion del reconocedor de voz
    
    #Extraccion de informacion del audio
    frecuencia_muestreo, senial = wavfile.read(filename) #Se extrae la taasa de muestreo, y un objeto con la informacion de la señal
    senial = senial / np.power(2, 15) #Se normaliza la señal
    #Se construye el eje de tiempo en milisegundos
    eje_del_tiempo = 1000 * np.arange(0, len(senial), 1) / float(frecuencia_muestreo)

    # Dibujar la señal de audio
    fig = plt.figure(figsize=(4, 3))    #Se define el tamaño del grafico
    plt.plot(eje_del_tiempo, senial, color='black') #Se grafican los datos
    plt.xlabel('Tiempo (milisegundos)') #Se pone nombre al eje x
    plt.ylabel('Amplitud') #Se pone nombre al eje y
    plt.title('Señal Entrada de Audio') #Se da el titulo del grafico.

    #Creación del grafico en forma de imagen
    imgdata = BytesIO() #Almacena informacion en bytes en una memoria de almacenamiento temporal
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)  # rewind the data
    drawing=svg2rlg(imgdata)

    shape = senial.shape


    with sr.AudioFile(filename) as source: #Abre el audio para convertirlo
        audio = r.listen(source)    #El reconocedor de voz escucha el audio

        try:   #Se usa el try en caso de que el audio no tenga nada para convertir
            print("Escuchando el audio. Por favor espere...")
            text = r.recognize_google(audio,language="es-ES") #Se usa el reconocedor de voz de google

            time.sleep(1.5)
            
            print('presione 1 para crear un pdf, press 2 para mostrar en consola. ')
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
            print("Lo siento , No puedo entender el audio")
    