#!/bin/env python3
Ver=0.2

from pytube import YouTube
from pytube.cli import on_progress
from argparse import ArgumentParser

# utils library
from utils.CheckLink import link_is_valid
from utils.MainTools import Download
from utils.InterruptHandler import sigint_handler
from utils.InterruptHandler import signal

signal.signal(signal.SIGINT, sigint_handler)

# parsing argvs and add link argv
parser = ArgumentParser(description=f"youtube url downloader {Ver}")
parser.add_argument('link')
parser.add_argument('--video','-v',action='store_true',help='download URL with video')
parser.add_argument('--audio','-a',action='store_true',help='download URL with only audio')
parser.add_argument('--dir','-d',action='store',type=str,help='set destination')

optionalparser = parser.add_argument_group( 'optional options' )
optionalparser.add_argument('--description','-desc',action='store_true',help='download URL with only audio')


argv_parsed = parser.parse_args()

video_link = argv_parsed.link
destination = argv_parsed.dir

if not link_is_valid:
    print("Enter valid video link")
    quit()

dl = Download(destination)
link = YouTube(str(video_link), on_progress_callback=on_progress)

dl.sort_resolutions(link)

if argv_parsed.description:
    print(Download.show_description(link))

if argv_parsed.video:
    dl.video(link)
elif argv_parsed.audio:
    Download.getcover(link)
    dl.audio(link)
else:
    print('set mediatype --video for video --audio for only audio')
    exit()

print(f'{link.title} Downloaded.')
