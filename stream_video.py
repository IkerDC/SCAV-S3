import os

def stream(filename, ip, port):
    #This function will stream a video.
    cmd = "ffmpeg -re -i " +filename+ " -c copy -f mpegts udp://" +ip+ ":"+port
    os.system(cmd)
    return True