#!/bin/env python3

from pytube import YouTube
from pytube.cli import on_progress
from argparse import ArgumentParser
from utils.CheckLink import link_is_valid
from utils.MainTools import sort_resolutions, mediatype, getcover
from utils.InterruptHandler import sigint_handler
from utils.InterruptHandler import signal

signal.signal(signal.SIGINT, sigint_handler)

# parsing argvs and add link argv
parser = ArgumentParser()
parser.add_argument('link')
parser.add_argument('--video','-v',action='store_true',help='download URL with video')
parser.add_argument('--audio','-a',action='store_true',help='download URL with only audio')
parser.add_argument('--dir','-d',action='store',type=str,help='set destination')
argv_parsed = parser.parse_args()

video_link = argv_parsed.link
destination = argv_parsed.dir

if not link_is_valid:
    print("Enter valid video link")
    quit()

link = YouTube(str(video_link), on_progress_callback=on_progress)

sort_resolutions(link)
if argv_parsed.video:
    mediatype(link,'video',destination)
elif argv_parsed.audio:
    getcover(link)
    mediatype(link,'audio',destination)
else:
    print('set mediatype --video for video --audio for only audio')
    exit()


print(f'{link.title} Downloaded.')
