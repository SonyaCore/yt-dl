#!/bin/env python3

# sys module
import os
import sys
import subprocess

from pytube import YouTube
from pytube.cli import on_progress

try: 
    # object creation using YouTube
    link = YouTube(str(sys.argv[1]),on_progress_callback=on_progress)
except: 
    print("Connection Error") #to handle exception 

def sort_resolutions():
    global video_resolutions
    global videos

    # Title of The Video
    print(link.title)

    # Thumbnail Image and Description
    print(f"{link.thumbnail_url}\n{link.description}")

    video_resolutions = []
    videos = []

    for stream in link.streams.order_by('resolution'):
        video_resolutions.append(stream)
        videos.append(stream)

    return video_resolutions, videos

import requests
import tempfile

def getcover():
    """get cover of url link"""
    global temp
    img_data = requests.get(link.thumbnail_url).content
    temp = tempfile.NamedTemporaryFile()
    with open(f'{temp.name}', 'wb') as handler:
        handler.write(img_data)

def mediatype():
    """media type selection and downloading media"""
    print("1: Video file with audio")
    print("2: Audio only")
    
    global media_type
    global video
    global out

    media_type = input()
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'
    
    if media_type == "1":
        while True:
            # Looping through the video_resolutions list to be displayed on the screen for user selection...
            i = 1
            for resolution in video_resolutions:
                print(f'{i}. {resolution}')
                i += 1

            choice = int(input('\nlists of avaliable output: '))
            
            # To validate if the user enters a number displayed on the screen...
            if 1 <= choice < i:
                resolution_to_download = video_resolutions[choice - 1]
                print(f"downloading {resolution_to_download}")

                # command for downloading the video
                out = videos[choice - 1].download(output_path = destination)

                break
            else:
                    print("Invalid choice!!\n\n")

    elif media_type == "2":
        video = link.streams.filter(only_audio = True).first()
        out = video.download(output_path = destination)
        try:
            base, ext = os.path.splitext(out)
            os.rename(out, base)
            getcover()

            cmd = f"ffmpeg -y -loop 1 -i '{temp.name}' -i '{os.path.realpath(base)}' -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest 'out.mp4'"
            subprocess.check_output(cmd, shell=True) 
            subprocess.call(cmd, shell=True)

            os.rename('out.mp4', base + '.mp3')
            os.remove(base)

            temp.close()
        except subprocess.CalledProcessError:
            print('ffmpeg are not installed')
            exit(1)

    else:
        print("Invalid selection.")
        exit(1)
    
sort_resolutions()
mediatype()
        
print(f'{link.title} Downloaded.')