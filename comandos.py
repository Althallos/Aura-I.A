import wikipedia
import pywhatkit
from voz import falar
from dowload_yt import download_yt

def executar_comando(executar):
    comando = executar
    try:
        #   Pesquisa sobre um determinado assunto na Wikipedia
        if('procure por' in comando) or ('pesquise por' in comando) or ('busque por' in comando) or \
            ('o que é' in comando) or ('o que e' in comando):
            palavra_chave = ['procure por', 'pesquise por', 'busque por', 'busque', 'procure', 'o que é', 'o que e']
            for i in palavra_chave:
                procurar = comando.replace(i, '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            falar(resultado, True)
            
        #   Reproduz vídeos, músicas e faz downloads em formato mp4 e mp3 do YouTube
        elif('toque' in comando) or ('rode' in comando) or ('música' in comando) or ('video' in comando) or ('vídeo' in comando) or \
            ('baixar' in comando) or ('baixe' in comando) or ('download' in comando) or ('baixa' in comando):
            palavra_chave = ['toque', 'rode', 'video', 'baixar', 'baixe', 'download']
            for i in palavra_chave:
                yt = comando.replace(i, '')
            if('baixar' in comando) or ('baixe' in comando) or ('download' in comando):
                resultado = pywhatkit.playonyt(yt)
                download_yt(resultado)

            else:
                resultado = pywhatkit.playonyt(yt)
            falar(comando, True)

        #   Funcionalidades da I.A
        elif('comando' in comando) or ('função' in comando) or ('funções' in comando) or ('opção' in comando) or ('opções' in comando):
            falar('Pesquisar informações pelo Wikipedia', True)
            falar('Executar vídeos e músicas do YouTube', True)
            falar('Baixar Videos e Músicas do YouTube', True)

        #   Sobre a I.A
        elif('quem é você' in comando) or ('quem e você' in comando) or ('o que é você' in comando) or \
            ('quem é você' in comando) or ('quem e você' in comando) or ('você é quem' in comando) or ('você e quem' in comando):
            falar('Meu Nome é Aura, Sou Uma I.A Projetada Para Atender Todas As Suas Necessidades.', True)
            falar('Verifique minhas opções de comando que possuo.', True)

        #   Desligar a I.A
        if('desativar' in comando) or ('desligar' in comando):
            falar('Desligando o Sistema.', True)
            return 'desligar'
    except:
        falar('Desculpe, não consigo executar o comando.', True)
        falar('Verifique minhas opções de comando que possuo', True)