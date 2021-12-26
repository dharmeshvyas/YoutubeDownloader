from pytube import YouTube
import os
import sys
sys.path.insert(0,"./src")
import check
import imgToAscii


print(imgToAscii.PrintAscii("./asserts/background.png"))

print("===================================================Welcome to Dv's Youtube Tools=======================================================")

URL = input(" Enter Youtube URL :")
while URL == "":
    URL=input("| Please Enter YouTube URL :")

while check.isValidURL(URL)==False:
        URL = input("Please Enter Valid URL :")

print("=============================================================Resolution================================================================")
print("""|                                ****************************                                                                           |
|                                *       1.144p             *                                                                           |
|                                *       2.240p             *                                                                           |
|                                *       3.360p             *                                                                           |
|                                *       4.480p             *                                                                           |
|                                *       5.720p             *                                                                           |
|                                *       6.1080p            *                                                                           |
|                                *       7.Audio            *                                                                           |
|                                ****************************                                                                           |""")
print("=======================================================================================================================================")
Resolution = input("Select Video Resolution :")
print("=======================================================================================================================================")
video = YouTube(URL)

if(Resolution=="1"):
    Resolution="160"
elif(Resolution=="2"):
    Resolution="133"
elif(Resolution=="2"):
    Resolution="134"
elif(Resolution == "4"):
    Resolution="135"
elif(Resolution == "5"):
    Resolution="136"
elif(Resolution == "6"):
    Resolution="137"
elif(Resolution == "7"):
    Resolution="251"
else:
    Resolution="136"
print("=====================================================Video Details====================================================================")
print(" *   Video Title :",video.title)
print("=======================================================================================================================================")
print(" *   Video Publish Date :",video.publish_date)
print("=======================================================================================================================================")
print(" *   Video Author :",video.author)
print("=======================================================================================================================================")
print(" *   Video Duration :",video.length)
print("=======================================================================================================================================")
print(" *   Video views :",video.views)
print("=======================================================================================================================================")
print(" *   Video description :",video.description)
print("=======================================================================================================================================")


video_streams = video.streams.get_by_itag(Resolution)
print("======================================================== Path =========================================================================")
getpath = input("Enter Location for downloading :")
print("=======================================================================================================================================")
if getpath is "":
    getpath = "./Downloaded"

print("=====================================================Downloading Section================================================================")
print("Download starting , Please wait...")
print("=======================================================================================================================================")
if(Resolution=="251"):

    Output_file  = video_streams.download(output_path=getpath)
    file_name,garbage = os.path.splitext(Output_file)
    newExtantion =  file_name + '.mp3'
    os.rename(Output_file,newExtantion)
else:
    video_streams.download(output_path=getpath)
print("=======================================================================================================================================")
print("Download complated in this ",getpath," Directory")
print("=======================================================================================================================================")


