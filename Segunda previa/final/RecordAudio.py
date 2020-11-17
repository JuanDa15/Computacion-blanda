#Library to access to recording functions
import pyaudio
#Library to make .wav files
import wave 
#Library used to play the audio
from playsound import playsound

def RecordAudio(RecordSeconds, filename):
    #Constants declarations
    FORMAT = pyaudio.paInt16 #set the sample format
    CHANNELS = 2 #Set the 2 channels for audio stereo, one channel for mono
    RATE = 48000 #Samples per second
    BUFFER = 1024 #Set the buffer size of 1024 samples
    RECORD_SECONDS = RecordSeconds #Audio duration
    FILENAME = filename #The filename output
    
    #Initialize pyaudio object
    p = pyaudio.PyAudio()
    
    #Open stream object as input & output
    stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = BUFFER)
    
    print("*recording")
    frames = [] #Initialize array to store frames
    
    #Store data in chuncks for n seconds
    for i in range(0,int(RATE/BUFFER * RECORD_SECONDS)):
        data = stream.read(BUFFER)
        #stream.write(data) heard audio while recording
        frames.append(data)
        
    print("* Done Recording")
    
    #Stop and close the stream
    stream.stop_stream()
    stream.close()
    
    #terminate pyaudio object
    p.terminate()
    
    #save audio file
    wf = wave.open(filename,"wb") #open file in 'write bytes' mode
    wf.setnchannels(CHANNELS) #set the channels
    wf.setsampwidth(p.get_sample_size(FORMAT)) #set the sample format
    wf.setframerate(RATE) #set the sample rate
    wf.writeframes(b"".join(frames)) #write the frames as bytes
    wf.close() #close the file
    
#Function to play de audio 
def PlayAudio(filename):
    playsound(filename)