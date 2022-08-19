#!/bin/env python3

from pytube import YouTube
from pytube.cli import on_progress
from argparse import ArgumentParser
from utils.CheckLink import link_is_valid
from utils.MainTools import sort_resolutions, mediatype


# parsing argvs and add link argv
parser = ArgumentParser()
parser.add_argument('link')
argv_parsed = parser.parse_args()

video_link = argv_parsed.link

if not link_is_valid:
    print("Enter valid video link")
    quit()


link = YouTube(str(video_link), on_progress_callback=on_progress)


sort_resolutions(link)
mediatype(link)

print(f'{link.title} Downloaded.')
