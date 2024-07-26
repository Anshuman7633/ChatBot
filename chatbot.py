import random
import webbrowser
import cv2
import subprocess
import sys
import datetime
import pyttsx3
import math

def open_website(website_url):
    webbrowser.open(website_url)

def open_camera():
    try:
        cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in webcam)

        while True:
            ret, frame = cap.read()
            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the camera stream
                break

        cap.release()
        cv2.destroyAllWindows()

    except cv2.error:
        print("Error: Could not access the camera. Make sure it is properly connected.")

def open_camera_app():
    if sys.platform.startswith('win32'):
        subprocess.run("start microsoft.windows.camera:", shell=True)
    elif sys.platform.startswith('darwin'):
        subprocess.run("open -a FaceTime", shell=True)
    elif sys.platform.startswith('linux'):
        print("Sorry, opening the camera app is not supported on Linux.")
    else:
        print("Sorry, opening the camera app is not supported on this platform.")

def show_datetime():
    current_datetime = datetime.datetime.now()
    print("Current Date and Time:")
    print(current_datetime.strftime("Date: %Y-%m-%d"))
    print(current_datetime.strftime("Time: %H:%M:%S"))
    print("Day:", current_datetime.strftime("%A"))

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def introduce_yourself():
    introduction = "Hello! I am a friendly chatbot. My name is Friday. I'm created by Anshuman Ankur Thakur. My purpose is to assist you with various tasks and have enjoyable conversations. Feel free to ask me anything!"
    print(introduction)
    speak(introduction)

def suggest_anime(genre):
    genre = genre.lower()
    search_query = f"best {genre} anime"
    search_url = f"https://www.google.com/search?q={search_query}"
    print(f"Opening Google search for: {search_query}")
    speak(f"Opening Google search for: {search_query}")
    webbrowser.open(search_url)

def add(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def integer_square_root(x):
    if x < 0:
        raise ValueError("Can't take the root of a negative number.")
    return math.isqrt(x)

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Integer Square Root")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3'):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtraction(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiplication(num1, num2))
        elif choice == '4':
            num = int(input("Enter the number: "))
            try:
                result = integer_square_root(num)
                print(f"The square root of {num} is: {result}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (y/n): ")
        if next_calculation != 'y':
            break

def chatbot():
    print("Hi! I'm Friday. What's your name?")
    user_name = input()
    print("Nice to meet you, " + user_name + "!")
    speak("Nice to meet you, " + user_name + "!")
    
    while True:
        print("How may I help you?")
        print("You can type 'help' to see the list of commands.")
        user_input = input("Text something: ").lower()
        
        if 'open website' in user_input:
            print("Which website would you like to open?")
            website_url = input("Enter the website URL: ")
            open_website(website_url)
        elif 'open camera' in user_input:
            open_camera()
        elif 'open camera app' in user_input:
            open_camera_app()
        elif 'show date and time' in user_input:
            show_datetime()
        elif 'introduce yourself' in user_input:
            introduce_yourself()
        elif 'suggest anime' in user_input:
            print("Sure! What genre are you interested in?")
            genre = input("Please enter the genre you are interested in: ")
            suggest_anime(genre)
        elif 'calculate' in user_input or 'calculation' in user_input:
            calculator()
        elif 'bye' in user_input:
            print("Goodbye! Have a great day!")
            speak("Goodbye! Have a great day!")
            break
        elif 'help' in user_input:
            print("Here are some commands you can use:")
            print("'open website' - Opens a specified website")
            print("'open camera' - Opens the default camera")
            print("'open camera app' - Opens the default camera application")
            print("'show date and time' - Displays the current date and time")
            print("'introduce yourself' - Introduces the chatbot")
            print("'suggest anime' - Suggests an anime based on the genre you provide")
            print("'calculate' or 'calculation' - Opens the calculator for basic operations")
            print("'bye' - Exits the chatbot")
        else:
            print("I'm sorry, I didn't understand that. Please try again or type 'help' to see the list of commands.")

if __name__ == "__main__":
    chatbot()
