import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)

pavel = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_ruRU_PavelM'

voices = engine.getProperty('voices')
voice = voices[0]

print(dir(voice))
print(voice)
v = voice.__class__(id=pavel, name='Microsoft Pavel - Russian (Russia)')
print(v)

voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices+[v])

# for voice in voices:
#     print(voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()
#engine.setProperty('voice', pavel)

#engine.say("Ну что поиграем")
#
engine.runAndWait()
# engine.say("I sssss speak this text")
# engine.runAndWait()