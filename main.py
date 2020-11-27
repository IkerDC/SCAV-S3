import os
import convert_codec as vc
import stream_video as streaming


def switch(exercice):
    if (exercice == "1"):
        print("Filename:")
        file = input()
        print("Introduce format from \"vp8\",\"vp9\",\"h265\" or \"av1\" (AV1 can take a long time)")
        cod = input()
        vc.codec(file, cod)
        return True
    elif (exercice == "2"):
        print("4 videos should be especified. Introduce the 4 filename, pressing ENTER each time a file name is introduced.")
        file1 = input()
        file2 = input()
        file3 = input()
        file4 = input()
        vc.visual(file1, file2, file3, file4)
        os.system("ffplay codec_compare.mp4")
        return True
    elif(exercice == "3"):
        print("Introduce filename (input.mp4):")
        file = input()
        print("Introduce IP of LAN (192.168.#.#):")
        IP = input()
        print("Introduce input port (####):")
        port = input()
        print("Stream "+ file+ " to " +IP+ ":" +port)
        print("To kill press [q]")
        streaming.stream(file, IP, port)
        return True
    else:
        return False

a = True
while(a):
    print("Select\n"
          "[1]: Change codec of a video to VP8, VP9, H265 or AV1\n"
          "[2]: Compare 4 different codec\n"
          "[3]: Stream a video to a local LAN\n"
          "[0]: Exit")
    ex = input()
    a = switch(ex)