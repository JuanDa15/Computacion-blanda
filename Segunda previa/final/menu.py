import RecordAudio 
import ConvertText 
from scipy.io import wavfile

def zero():
    print('write record time duration: ')
    RECORD_TIME = input()
    print('write the name of the output file: ')
    name = input()
    filename = name + '.wav'
    type,rate = RecordAudio.RecordAudio(int(RECORD_TIME),filename)

    print('Press 1 if want to heard the audio or 0 to continue')
    option = input()
    if(int(option) == 1):
        RecordAudio.PlayAudio(filename)
    ConvertText.ConvertAUDIO(filename,name,[type, RECORD_TIME ,str(rate)])
    


def one():
    print("1. be sure the audio file is in this folder, else write the complete direction")
    print("press 1 if the file is in this folder.")
    print("press 2 if is in other folder. ")
    option = input()
    if(int(option) == 1):
        print("write the file name: ")
        name = input()
        filename = name + '.wav'
        frecuencia_muestreo, senial = wavfile.read(path)
        ConvertText.ConvertAUDIO(filename,name,[str(senial.dtype),str(round(senial.shape[0] / float(frecuencia_muestreo),2)),str(frecuencia_muestreo)])
    elif(int(option) == 2):
        print("write the full file path: ")
        path = input()
        frecuencia_muestreo, senial = wavfile.read(path)
        ConvertText.ConvertAUDIO(path,'textfile',[str(senial.dtype),str(round(senial.shape[0] / float(frecuencia_muestreo),2)),str(frecuencia_muestreo)])


def two():
    

switcher = {
    0:zero,
    1:one,
    2:two
}

def menu(argument):
    func = switcher.get(argument,"nothing")
    return func()
        
        
        
def main():
    print('Ingrese la opción que necesita:')
    print('0: Record voice')
    print('1: From and external audio')
    option = input()
    if((int(option) == 0) or (int(option) == 1)):
        menu(int(option))
    else:
        main()
        
main()