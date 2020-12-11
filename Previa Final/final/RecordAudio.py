#Library to access to recording functions
import pyaudio
#Library to make .wav files
import wave 
#Library used to play the audio
from playsound import playsound

def Record(RecordSeconds, filename):
    #Constants declarations
    FORMAT = pyaudio.paInt16 #Se define el tipo de muestra
    CHANNELS = 1 #Se definen 2 canales para un audio estereo, o un canal para audio mono
    RATE = 48000 #Muestras por segundo
    BUFFER = 1024 #Se define el tamaña de la memoria temporal para las muestras
    RECORD_SECONDS = RecordSeconds #Audio duration
    FILENAME = filename #Nombre del archivo de salida
    
    #Inicializacion del objeto de pyaudio
    p = pyaudio.PyAudio()
    
    #Se abre el objeto en formato de entrada y salida
    #Y se asignan las caracteristicas del audio
    stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = BUFFER)
    
    print("*Grabando")

    frames = [] #Inicializa el array para almacenar la informacion de la grabación
    
    #Almacene datos en trozos durante n segundos
    for i in range(0,int(RATE/BUFFER * RECORD_SECONDS)):
        data = stream.read(BUFFER) #Almacenar la informacion en data
        #stream.write(data) Escuchar el audio mientras se graba
        frames.append(data) #se agrega al arreglo de frames la informacion almacenada en data
        
    print("* Grabacion completa")
    
    #Para y se cierra la grabación
    stream.stop_stream()
    stream.close()
    #Finalizacion del objeto de pyaudio
    p.terminate()
    
    #Guardar el archivo de audio
    wf = wave.open(filename,"wb") #Abre un archivo en modo 'write bytes' 
    wf.setnchannels(CHANNELS) #Se definen la cantidad de canales del audio
    wf.setsampwidth(p.get_sample_size(FORMAT)) #Establece el formato del audio
    wf.setframerate(RATE) #Establece la frecuencia de muestreo
    wf.writeframes(b"".join(frames)) #escribe los frames como bytes
    wf.close() #Cierra el archivo

    return "paInt16",RATE
    
#Function to play de audio 
def PlayAudio(filename):
    playsound(filename)