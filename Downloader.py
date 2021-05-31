from pytube import YouTube    # install the required module
# "pip install pytube"

link = input("Enter Your YouTube URL :")
yt = YouTube(link)
videos = yt.streams.all()     # this will stream all the format available for the video
video = list(enumerate(videos))    # this will be index all the format in the list starting with zero

for i in video:
    print(i)
    # this will print all the available format of video with proper index

print("enter the desired option to download the format")
dn_option = int(input("enter the option :"))   # ask user that which format he wanted to download
dn_video = videos[dn_option]
dn_video.download()   # for downloading the video
print("download successfully")
