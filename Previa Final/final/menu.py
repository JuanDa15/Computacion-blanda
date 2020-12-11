import RecordAudio
import ConvertText
import ImageEscaner
from scipy.io import wavfile
import ImageEscaner
import ConvertText

def zero():
    print('Escriba la duracion del audio: ')
    RECORD_TIME = input()
    print('Escriba el nombre para el archivo: ')
    name = input()
    filename = name + '.wav'
    type,rate = RecordAudio.Record(int(RECORD_TIME),filename)

    print('presione 1 si quiere escucharlo o 0 para continuar')
    option = input()
    if(int(option) == 1):
        RecordAudio.PlayAudio(filename)
    ConvertText.ConvertAUDIO(filename,name,[type, RECORD_TIME ,str(rate)])
    


def one():
    print("Presione 1 si el audio esta en esta carpeta.")
    print("Presione 2 si esta en una carpeta externa. ")
    option = input()
    if(int(option) == 1):
        print("Escriba el nombre del archivo: ")
        name = input()
        filename = name + '.wav'
        frecuencia_muestreo, senial = wavfile.read(filename)
        ConvertText.ConvertAUDIO(filename,name,[str(senial.dtype),str(round(senial.shape[0] / float(frecuencia_muestreo),2)),str(frecuencia_muestreo)])
    elif(int(option) == 2):
        print("Escribe la ruta completa de la imagen: ")
        path = input()
        frecuencia_muestreo, senial = wavfile.read(path)
        ConvertText.ConvertAUDIO(path,'textfile',[str(senial.dtype),str(round(senial.shape[0] / float(frecuencia_muestreo),2)),str(frecuencia_muestreo)])


def two():
    print("Escribe la ruta completa de la imagen: ")
    opcion = input()
    ImageEscaner.Scanner(str(opcion))

switcher = {
    0:zero,
    1:one,
    2:two
}

def menu(argument):
    func = switcher.get(argument,"nada")
    return func()
        
        
        
def main():
    print('Ingrese la opción que necesita:')
    print('0: Grabar audio')
    print('1: Audio externo')
    print('2: Escanear imagen')
    option = input()
    if((int(option) == 0) or (int(option) == 1) or (int(option) == 2)):
        menu(int(option))
    else:
        main()
        
main()