from pytube import YouTube
from pytube.cli import on_progress
import os
import sys
from time import sleep

def papai():
    
    while True:
    
     link = input("Insira o link da Música: ")

     yt = YouTube(link, on_progress_callback = on_progress)

     print("Titulo = ", yt.title)
     print("Baixando...")

     ys = yt.streams.get_audio_only()
     out_file = ys.download()
     base, ext = os.path.splitext(out_file)
     new_file = base + '.mp3'
     os.rename(out_file, new_file)
     sleep(1)
     print('\n')
     print('Arquivo Baixado!')
     print('\n')
     mamae()

def mamae():
    
    while True:
  
     print('Obs:\nUse 1 Para Sim\nUse 2 Para Não.')
     enter = input('Deseja baixar outra Música?: ')
   
     if enter == '2':
        print('Good Bye!')
        sleep(1)
        fechar()

     elif enter == '1':
        sleep(1)
        os.system('cls')
        papai()

     else:
        print('Opção Incorreta!')
        sleep(2)
        mamae()
  
      
def fechar():
    sys.exit()

papai()
mamae()

