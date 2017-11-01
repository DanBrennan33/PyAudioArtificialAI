import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

running = True

# Function to call text to say in terminal via subprocess

def say(text):
    subprocess.call('say ' + text, shell=True)



# Defining chunks to be read
# opening the file as binary wave file
# Instantiate the pyaudio class

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    
    # Create stream for audio
    # Open file through pyaudio
    # Pass arugments to stream audio
    
    stream = pa.open(
            format=pa.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )
    
    # Read frames at the intial chunk of 1024
    
    data_stream= wf.readframes(chunk)
    
    # Continue reading at next chunk of frames
    
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    # Close steam and pyaudio class

    stream.close()
    pa.terminate()
 
# Uncomment to play wav files 
    
#play_audio("./AudioFiles/wet.wav")
#play_audio("./AudioFiles/suppressed.wav")


# Intialize Speech Recognizer

r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    # Notification that program started
    play_audio("./AudioFiles/short-notice.wav")

    # Output to initiate listening to microphone
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
    # Notification that program ended
    play_audio("./AudioFiles/served.wav")

    command = ""
    
    # Initialize audio recording variable or exception statement
    
    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand audio.")
        
    # Print recording to output    
    
    print("Your command: ")
    print(command)
    if command in ["quit", "exit", "bye", "goodbye", "goodnight"]:
        global running
        running = False
        
        
    cmd.discover(command)
    #say('You said: ' + command)
    
while running == True:
    initSpeech()


