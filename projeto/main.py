from voz import falar, microfone
from comandos import executar_comando

falar('Olá, Meu Nome é Aura Uma I.A Criada Para Te Ajudar.', True)
falar('Para Ver Os Possíveis Comandos, Fale AJUDA!', True)
def listen_command():
    while True:
        try:
            comando = microfone()
            print(comando, True)
            comando = comando.replace('Aura', '')
            return comando
        except Exception as e:
            falar(f'Não Entendi Poderia Repetir!', True)
            
while True:
    comando = executar_comando(listen_command())
    #   Desligar a I.A
    if('desligar' == comando):
        break
    