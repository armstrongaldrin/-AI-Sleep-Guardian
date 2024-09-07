import pyttsx3

# Initialize the pyttsx3 engine
eng = pyttsx3.init()

# Get the available voices
voices = eng.getProperty('voices')

# Check if there are at least 3 voices
if len(voices) >= 3:
    # Set the desired voice (you can choose any of the available ones)
    eng.setProperty('voice', voices[2].id)  # Example: use the third voice (index 2)
else:
    print("Not enough voices available, using the default voice.")

# Test the selected voice
eng.say("Welcome to Sleep Apnea Guardian. My name is Apnea!")
eng.runAndWait()

