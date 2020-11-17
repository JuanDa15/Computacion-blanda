import RecordAudio 
import ConvertText 

def zero():
    print('write record time duration: ')
    RECORD_TIME = input()
    print('write the name of the output file: ')
    name = input()
    filename = name + '.wav'
    RecordAudio.RecordAudio(int(RECORD_TIME),filename)

    print('Press 1 if want to heard the audio or 0 to continue')
    option = input()
    if(int(option) == 1):
        RecordAudio.PlayAudio(filename)
        
    ConvertText.ConvertAUDIO(filename,name)


def one():
    print("1. be sure the audio file is in this folder, else write the complete direction")
    print("press 1 if the file is in this folder.")
    print("press 2 if is in other folder. ")
    option = input()
    if(int(option) == 1):
        print("write the file name: ")
        name = input()
        filename = name + '.wav'
        ConvertText.ConvertAUDIO(filename,name)
    elif(int(option) == 2):
        print("write the full file path: ")
        path = input()
        ConvertText.ConvertAUDIO(path,'textfile')

switcher = {
    0:zero,
    1:one
}

def menu(argument):
    func = switcher.get(argument,"nothing")
    return func()
        
        
        
def main():
    print('Ingrese la opción que necesita:')
    print('0: Record your voice')
    print('1: From and external audio')
    option = input()
    if((int(option) == 0) or (int(option) == 1)):
        menu(int(option))
    else:
        main()
        
main()