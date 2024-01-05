from pytube import YouTube
from voz import falar, microfone

def opcao():
    falar('\033[0;31mDownload De MP4 e MP3(Videos e Áudios)\033[m', True)
    falar('\033[0;34m1\033[m - MP4 [Vídeo] (720p)', True)
    falar('\033[0;34m2\033[m - MP3 [Áudio] (160kbps)', True)
    falar('Para SAIR Fale CANCELAR!', True)
    falar('Para Ver as Opções de Download Novamente Fale OPÇÃO!', True)

def download_yt(nome, tipo='mp4'):
    opcao()
    while True:
        try:
            falar('Qual Formato de Download Gostaria de Baixar: ', True)
            formato = microfone()
            falar(formato, True)
            if('mp4' in formato) or ('video' in formato) or ('vídeos' in formato) or ('1' in formato) or ('um' in formato):
                falar('Download Do Arquivo MP4', True)
                YouTube(nome).streams.filter(res=('720p')).first().download()
                falar('Download Concluído', True)
                break
            elif('mp3' in formato) or ('audio' in formato) or ('áudio' in formato) or ('musica' in formato) or ('música' in formato) or \
                ('2' in formato) or ('dois' in formato):
                falar('Download Do Arquivo MP3', True)
                YouTube(nome).streams.filter(only_audio=True, abr=('160kbps')).first().download()
                falar('Download Concluído', True)
                break
            elif('Cancelar' in formato):
                break
            elif('opção' in formato) or ('opções' in formato):
                opcao()
        except Exception:
            falar('Escolha de Download Invalido!')

