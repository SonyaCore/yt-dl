#!/bin/env python3

# sys module
import os
import sys

from pytube import YouTube
from pytube.cli import on_progress

try: 
    # object creation using YouTube
    # which was imported in the beginning
    link = YouTube(str(sys.argv[1]),on_progress_callback=on_progress)
except: 
    print("Connection Error") #to handle exception 

def mediatype():
        print("1: Video file with audio (.mp4)")
        print("2: Audio only (.mp3)")
        global media_type
        global video
        
        media_type = input()
        if media_type == "1":
            video = link.streams.first()

        elif media_type == "2":
            video = link.streams.filter(only_audio = True).first()

        else:
            print("Invalid selection.")
            exit(1)
mediatype()


print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
print('FileSize : ' + str(round(video.filesize/(1024*1024))) + 'MB')
out = video.download(output_path = destination)

import requests
img_data = requests.get(link.thumbnail_url).content
with open('cover', 'wb') as handler:
    handler.write(img_data)

import subprocess

if media_type == "1":
    base, ext = os.path.splitext(out)
    file = base + '.mp4'
    os.rename(out,file)

elif media_type == "2":
    try:
        base, ext = os.path.splitext(out)
        os.rename(out, 'base')

        cmd = f"ffmpeg -y -loop 1 -i cover -i '{os.path.realpath('base')}' -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest 'out.mp4'"
        subprocess.check_output(cmd, shell=True) 
        subprocess.call(cmd, shell=True)
        file = base + '.mp3'
        os.rename('out.mp4', file)
        os.remove('base')
        os.remove('cover')
    except ValueError:
        None
print(f'{link.title} Downloaded.')
