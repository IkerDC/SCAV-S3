import os

def codec(filename, codec):
    #Function to change the codec between vp8, vp9, h265, av1. The code used different libraries.
    if(codec == "vp8"):
        cmd = "ffmpeg -i " +filename+ " -c:v libvpx -b:v 1M -c:a libvorbis VP8_video.webm"
        os.system(cmd)
    elif(codec == "vp9"):
        cmd = "ffmpeg -i " +filename+ " -c:v libvpx-vp9 -b:v 2M VP9_video.webm"
        os.system(cmd)
    elif(codec == "h265"):
        cmd = "ffmpeg -i " +filename+ " -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k H265_video.mp4"
        os.system(cmd)
    elif(codec == "av1"):
        cmd = "ffmpeg -i " +filename+ " -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental AV1_video.mkv"
        os.system(cmd)
    else:
        print("The codec introduced is not available.")

def visual(filename1, filename2, filename3, filename4):
    #this function will combine 4 videos of different format or the same
    cmd1 = "ffmpeg -ss 0 -i " +filename1+ " -ss 0 -i "+filename3+" -filter_complex vstack left.mp4"
    cmd2 = "ffmpeg -ss 0 -i " +filename2+ " -ss 0 -i " +filename4+ " -filter_complex vstack right.mp4"
    cmd3 = "ffmpeg -i left.mp4 -i right.mp4 -filter_complex hstack -i audio.mp4 codec_compare.mp4"
    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)
    os.remove("left.mp4")
    os.remove("right.mp4")




