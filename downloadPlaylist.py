from __future__ import unicode_literals
import subprocess
import shlex

location = "C:/Users/srira/Music/"

folderName = input("Enter playlist name ")
playlist = input("Enter playlist URL ")

print("If you would like to choose a custom location, enter 1. Otherwise, press any other key, and the playlist will be downloaded to the following directory " + location)

decision = input();

if(decision == 1):
    location = ("Enter custom path ");



path_template = location + folderName + "/" + "%(title)s.%(ext)s"

command = "youtube-dl --extract-audio -i --audio-format mp3 --audio-quality 0 --no-part --no-mtime --embed-thumbnail --add-metadata -o \""+path_template+"\" \""+ playlist+ "\" -v --postprocessor-args \"-id3v2_version 3\""

process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
output, error = process.communicate()

# ydl_opts = get_ydl_options(path_template)

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([playlist])



print("success")
