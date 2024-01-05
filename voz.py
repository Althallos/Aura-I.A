import pyttsx3
import speech_recognition as sr


#   Voz da I.A
maquina = pyttsx3.init()

def falar(frase, mensagem = False):
    if mensagem == True:
        print(frase)
    maquina.say(frase)
    maquina.runAndWait()

#   Microfone
voz = sr.Recognizer()

def microfone():
    with sr.Microphone() as source:
        voz.adjust_for_ambient_noise(source)
        falar('Escutando...', True)
        audio = voz.listen(source)
        comando = voz.recognize_google(audio, language='pt-BR')
        comando = comando.lower()
    return comando
