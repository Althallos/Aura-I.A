from voz import falar, microfone
from comandos import executar_comando


def listen_command():
    while True:
        try:
            comando = microfone()
            falar(comando, True)
            comando = comando.replace('Aura', '')
            return comando
        except Exception as e:
            falar(f'Não Entendi Poderia Repetir!', True)
            
while True:
    comando = executar_comando(listen_command())
    #   Desligar a I.A
    if('desligar' == comando):

        break