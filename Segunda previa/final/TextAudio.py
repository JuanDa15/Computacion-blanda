import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Di algo.')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('lo que dijiste fue: {}'.format(text))
    except:
        print('lo siento no puedo entendderlo')


        print HKEY_LOCAL_MACHINE