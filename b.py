import ctypes
import pyjokes
import pyttsx3
import cv2
import speech_recognition as sr
import os
import sys

def get_joke():
    """Fetches and returns a joke using the pyjokes library."""
    try:
        joke = pyjokes.get_joke()
        return joke
    except Exception as e:
        return f"Error fetching joke: {e}"

def process_query(query):
    """Processes the voice command and performs the corresponding action."""
    if 'lock window' in query.lower():
        speak("Locking the device")
        ctypes.windll.user32.LockWorkStation()
    elif 'tell me a joke' in query.lower():
        joke = get_joke()
        speak(joke)
        print(joke)
    elif 'open camera' in query.lower() or 'camera' in query.lower():
        open_camera()
    
    elif "no thanks" or "no" or "exit" in query:
            speak("thanks for using me sir ,have a good day")
            sys.exit()

def speak(message):
    """Converts text to speech using pyttsx3."""
    try:
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")

def open_camera():
    """Opens the webcam and displays the feed until the 'ESC' key is pressed."""
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture image.")
                break

            cv2.imshow('Webcam', frame)

            # Wait for 50ms and check if the 'ESC' key is pressed
            if cv2.waitKey(50) & 0xFF == 27:  # 27 is the ASCII code for the 'ESC' key
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

def listen_for_command():
    """Listens for a voice command and returns the recognized text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing command...")
        command = recognizer.recognize_google(audio)
        print(f"Command recognized: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the command.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

# Example usage
if __name__ == "__main__":
    while True:
        command = listen_for_command()
        process_query(command)
