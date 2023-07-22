import random
import webbrowser
import cv2
import subprocess
import sys
import datetime
import pyttsx3

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
    anime_by_genre = {
        "action": ["Naruto", "Attack on Titan", "My Hero Academia", "One Punch Man", "Bleach"],
        "adventure": ["Hunter x Hunter", "One Piece", "Sword Art Online", "Fullmetal Alchemist", "Fairy Tail"],
        "comedy": ["One Piece", "Gintama", "Konosuba: God's Blessing on This Wonderful World!", "Nichijou", "KonoSuba"],
        "fantasy": ["Fate/stay night", "Black Clover", "The Rising of the Shield Hero", "Re:Zero - Starting Life in Another World", "Overlord"],
        "drama": ["Your Lie in April", "Clannad", "Anohana: The Flower We Saw That Day", "Violet Evergarden", "A Silent Voice"],
        "romance": ["Toradora!", "Clannad", "Your Lie in April", "Fruits Basket", "My Love Story!!"],
    }

    anime_summaries = {
        "Naruto": "Naruto is a young ninja who seeks recognition from his peers and dreams of becoming the Hokage, the leader of his village.",
        "Attack on Titan": "In a world where humanity resides within enormous walled cities to protect themselves from Titans, gigantic humanoid creatures, a young boy named Eren Yeager vows to rid the world of the Titans and seek revenge for the destruction of his home.",
        "My Hero Academia": "In a world where people with superpowers (known as Quirks) are the norm, a boy without them desperately wants to enroll in a prestigious hero academy and learn what it really means to be a hero.",
        "One Punch Man": "Saitama is a superhero who can defeat any opponent with a single punch, but he is bored and frustrated because he can find no worthy opponents.",
        "Bleach": "Ichigo Kurosaki, a teenager with the ability to see ghosts, accidentally obtains soul reaper powers and must protect the living world from evil spirits known as Hollows.",
        "Hunter x Hunter": "Gon Freecss sets out on a journey to become a hunter, a special title that allows him to search for his missing father, but the path to becoming a hunter is full of challenges.",
        "One Piece": "Monkey D. Luffy and his pirate crew set out on an adventure to find the ultimate treasure known as One Piece and become the Pirate King.",
        "Sword Art Online": "Players of a virtual reality MMORPG get trapped inside the game, and to escape, they must clear all 100 floors of the game's tower.",
        "Fullmetal Alchemist": "Two brothers, Edward and Alphonse Elric, use alchemy in their quest to search for the Philosopher's Stone to restore their bodies after a failed alchemy experiment.",
        "Fairy Tail": "Lucy Heartfilia joins the Fairy Tail guild and goes on adventures with her friends, experiencing both joy and sorrow as they face various challenges.",
        "Gintama": "In an alternate-history Japan invaded by aliens, the samurai Gintoki Sakata and his friends take on odd jobs to make a living and protect their freedom.",
        "Konosuba: God's Blessing on This Wonderful World!": "Kazuma Sato, after dying a comically absurd death, is given the chance to start a new life in a fantasy world, but it's not quite the adventure he expected.",
        "Nichijou": "The daily lives of three friends and their fellow high school students are anything but ordinary as they encounter strange phenomena and absurd situations.",
        "KonoSuba": "After dying a laughable and pathetic death on his way back from buying a game, Kazuma Satou is given the choice to go to heaven or start life in a fantasy world.",
        "Fate/stay night": "Shirou Emiya is thrust into a world of danger and deception, where he must participate in the Holy Grail War, a deadly tournament to obtain a wish-granting artifact.",
        "Black Clover": "Asta, a boy born without magic in a world where magic is everything, aims to become the Wizard King, the greatest mage in the kingdom.",
        "The Rising of the Shield Hero": "Iwatani Naofumi is summoned to another world as one of the four legendary heroes, but he is soon betrayed and must rise to become the Shield Hero.",
        "Re:Zero - Starting Life in Another World": "Subaru Natsuki is transported to a fantasy world, where he discovers he has the ability to reset time whenever he dies, leading to countless challenges.",
        "Overlord": "Momonga, an ordinary salaryman, is transported to a virtual reality game world as his in-game character and decides to rule the world as the all-powerful overlord.",
        "Your Lie in April": "A piano prodigy suffering from the trauma of his mother's death meets a spirited violinist who helps him rediscover his love for music.",
        "Clannad": "Tomoya Okazaki meets a strange girl named Nagisa Furukawa, and their encounter changes their lives as they experience love, friendship, and hardships together.",
        "Anohana: The Flower We Saw That Day": "A group of childhood friends reunite to help the ghost of a deceased friend fulfill her wish and find closure for their unresolved feelings.",
        "Violet Evergarden": "Violet Evergarden, a former soldier, becomes an Auto Memory Doll and helps people express their feelings through beautifully written letters.",
        "A Silent Voice": "Shoya Ishida, a former bully, seeks redemption and attempts to reconnect with Shoko Nishimiya, a deaf girl he tormented in elementary school.",
        "Toradora!": "Ryuuji Takasu and Taiga Aisaka team up to help each other confess to their crushes, but their plan leads to unexpected feelings and complications.",
        "Fruits Basket": "After Tohru Honda learns the family secret of the Sohma family, she becomes involved in their lives and helps them break the curse that turns them into animals of the Chinese zodiac.",
        "My Love Story!!": "Takeo Gouda, a tall and muscular guy, falls in love with the sweet and petite Rinko Yamato, and their relationship faces numerous challenges and heartwarming moments.",
    }

    genre = genre.lower()

    if genre in anime_by_genre:
        suggestions = anime_by_genre[genre]
        suggestion = random.choice(suggestions)
        print(f"Based on the {genre} genre, I suggest you watch: {suggestion}")
        speak(f"Based on the {genre} genre, I suggest you watch: {suggestion}")

        if suggestion in anime_summaries:
            summary = anime_summaries[suggestion]
            print("Summary:", summary)
            speak("Summary: " + summary)
        else:
            print("Sorry, I don't have a summary for this anime.")
            speak("Sorry, I don't have a summary for this anime.")
    else:
        print("Sorry, I don't have any anime suggestions for that genre.")
        speak("Sorry, I don't have any anime suggestions for that genre.")

def chatbot():
    responses = {
        "hello": ["Hi there!", "Hello!", "Hi!"],
        "how are you": ["I'm doing well, thank you!", "I'm good, thanks for asking!"],
        "what's your name": ["My name is Friday!", "I'm Friday!"],
        "introduction": [introduce_yourself],
        "open website": ["Sure! Which website would you like me to open?", "Opening the website you requested."],
        "open camera": ["Sure! Opening the camera.", "Let's open the camera."],
        "open camera app": ["Sure! Opening the camera app.", "Let's open the camera app."],
        "show date and time": ["Sure! Here's the current date and time.", "Let me show you the date and time."],
        "suggest anime": ["Sure! What genre are you interested in?", "I can suggest anime based on different genres. What genre do you prefer?"],
        "bye": ["Goodbye!,sir have a nice day", "Bye!"]
    }

    print("Hi! I'm Friday. What's your name?")
    speak("Hi! I'm Friday. What's your name?")
    name = input()
    print(f"Nice to meet you, {name}!")
    speak(f"Nice to meet you, {name}!")
    print("How may I help you?")
    speak("How may I help you?")

    while True:
        user_input = input("Text something: ")

        if user_input.lower() == "bye":
            print(random.choice(responses["bye"]))
            speak(random.choice(responses["bye"]))
            break
        elif "open website" in user_input.lower():
            print(random.choice(responses["open website"]))
            speak(random.choice(responses["open website"]))
            website_url = input("Please enter the website URL: ")
            open_website(website_url)
        elif "open camera" in user_input.lower():
            print(random.choice(responses["open camera"]))
            speak(random.choice(responses["open camera"]))
            open_camera()
        elif "open camera app" in user_input.lower():
            print(random.choice(responses["open camera app"]))
            speak(random.choice(responses["open camera app"]))
            open_camera_app()
        elif "show date and time" in user_input.lower():
            print(random.choice(responses["show date and time"]))
            speak(random.choice(responses["show date and time"]))
            show_datetime()
        elif "introduce yourself" in user_input.lower():
            introduce_yourself()
        elif "suggest anime" in user_input.lower():
            print(random.choice(responses["suggest anime"]))
            speak(random.choice(responses["suggest anime"]))
            user_genre = input("Please enter the genre you are interested in: ")
            suggest_anime(user_genre)
        else:
            for key in responses:
                if key in user_input.lower():
                    if callable(responses[key]):
                        responses[key]()
                    else:
                        print(random.choice(responses[key]))
                        speak(random.choice(responses[key]))
                    break

chatbot()
