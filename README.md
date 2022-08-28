# yt-dl
youtube video/audio downloader is a program to download youtube urls with specific resolution or format

yt-dl uses pytube library to provide all of the functionality


> only youtube links are supported

## How to Run :
```
# clone repo
git clone https://github.com/SoniaCore/yt-dl.git
cd yt-dl

# install requirements
pip install -r requirements.txt
```
```
# run ytbot
ytbot.py 'https://youtu.be/EngW7tLk6R8' #youtube-url --video #mediatype
```
## Options:
```
--video -v download URL with video
--audio -a download URL with only audio
--dir   -d set destination for saving file

--description -desc show url description
```
### Todo List

- [ ] Error Handeling
- [x] Link Validation
- [x] better MediaType Selection
- [ ] Simpler Stream Selection
