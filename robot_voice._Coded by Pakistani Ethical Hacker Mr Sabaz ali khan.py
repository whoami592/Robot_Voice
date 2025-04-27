import pyttsx3

def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties (optional: adjust voice, rate, and volume)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    
    # Get available voices and set a robotic-sounding voice (default voice is used here)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index for different voices (0 or 1 usually)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Main program
if __name__ == "__main__":
    print("Type the text you want the AI to say (or 'quit' to exit):")
    while True:
        user_input = input("Enter text: ")
        if user_input.lower() == 'quit':
            print("Exiting program.")
            break
        speak(user_input)