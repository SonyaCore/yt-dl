import requests
import tempfile
import os
import sys
import subprocess


class Download():
    def __init__(self,destination):
        "media type selection and downloading media"
        self.destination = destination
        if not destination:
            destination = f'{sys.path[0]}/'

    
    def sort_resolutions(self,link):
        "sort stream order"

        # Title of The Video
        print(link.title)

        # Thumbnail Image
        print(link.thumbnail_url)

        self.video_resolutions = []
        self.videos = []

        for stream in link.streams.order_by('resolution'):
            self.video_resolutions.append(stream)
            self.videos.append(stream)

        return self.video_resolutions, self.videos

    def video(self,link):
        while True:
            # Looping through the video_resolutions list to be displayed on the screen for user selection...
            i = 1
            for resolution in self.video_resolutions:
                print(f'{i}. {resolution}')
                i += 1

            choice = int(input('\nlists of avaliable output: '))

            # To validate if the user enters a number displayed on the screen...
            if 1 <= choice < i:
                resolution_to_download = self.video_resolutions[choice - 1]
                print(f"downloading {resolution_to_download}")

                # command for downloading the video
                self.videos[choice - 1].download(output_path=self.destination)

                break
            else:
                print("Invalid choice!!\n\n")
                
    def audio(self,link):
            video = link.streams.filter(only_audio=True).first()
            out = video.download(output_path=self.destination)
            try:
                base, ext = os.path.splitext(out)
                os.rename(out, base)

                cmd = f"ffmpeg -y -loop 1 -i '{temp.name}' -i '{os.path.realpath(base)}' -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest 'out.mp4'"
                subprocess.check_output(cmd, shell=True)
                subprocess.call(cmd, shell=True)

                os.rename('out.mp4', base + '.mp3')
                os.remove(base)

                temp.close()
            except subprocess.CalledProcessError:
                print('ffmpeg are not installed')
                exit(1)

    def getcover(link):
        "get cover of url link"
        global temp
        img_data = requests.get(link.thumbnail_url).content
        temp = tempfile.NamedTemporaryFile()
        with open(f'{temp.name}', 'wb') as handler:
            handler.write(img_data)

    def show_description(link):
        "show video description"
        return (f"\n{link.description}")
