import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

from gemini import generate_description_from_text, MODEL_TEXT

recognizer = sr.Recognizer()
engine = pyttsx3.init()

voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0"
engine.setProperty('voice', voice_id)


def execute_command():
    try:
        with sr.Microphone() as source:
            print("Listening..")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="pt-BR").lower()
            return command
    except sr.UnknownValueError as e:
        print(f"Could not understand the audio; {e}")
    except sr.RequestError as e:
        print(f"Error requesting speech recognition service results; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def user_voice_command():
    while True:
        command = execute_command()
        if command:
            if "horas" in command:
                print("buscando horas...")
                current_time = datetime.datetime.now().strftime("%H:%M")
                engine.say("Agora são " + current_time)
                engine.runAndWait()
            elif "procure por" in command:
                print("procurando informação...")
                search_query = command.replace("procure por", "")
                wikipedia.set_lang("pt")
                result = wikipedia.summary(search_query, 2)
                print(result)
                engine.say(result)
                engine.runAndWait()
            elif "toque" in command:
                print("tocando...")
                song = command.replace("toque", "")
                result = pywhatkit.playonyt(song)
                print(result)
                engine.say("Tocando música")
                engine.runAndWait()
            elif "olá" in command:
                print("Olá")
                engine.say("Olá, tudo bem?")
                engine.runAndWait()
            elif "parar" in command:
                print("Até logo!")
                engine.say("Até logo!")
                engine.runAndWait()
                break
            elif "curiosidade" in command:
                print("buscando uma curiosidade...")
                result = generate_description_from_text("Me retorne uma curiosidade", MODEL_TEXT)
                print(result)
                engine.say(result)
                engine.runAndWait()


user_voice_command()
