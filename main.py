import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    text = input("Enter your anything to speak")
    if text == "q":
        break
    speak.Speak(text)