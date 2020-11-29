### SCAV-S3

This code is intended to satisfy the requirements of the seminar 3 from the course Audio and Video Encoding Systems (University Pompeu Fabra, 2020).


<img src="https://upload.wikimedia.org/wikipedia/commons/5/53/Logo_UPF.jpg" width="128" height="44" />

# Installation
This code was writen in Python via IDE PyCharm (in Windows), thus Python is expected to be installed. Use the main.py along with the rest of .py where the opretaions are written. In the video folder there are some videos to test the program as well as some videos showcasing the output of the code. 

# Requirements
None external packages form Python are required. This code only makes usage of the *os* and *ffmpeg* which should be instaled following this page [Install FFmpeg](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu).

# Operations
* **Converte a video to VP8, VP9, H265 & AV1**: This first operation is written on the *convert_codec.py* script. The function will converte any given video to whatever of the 4 codec selectes with each corresponing format. The codec to choose from is untroduced as input from the user, aswell as teh selected video. The convertion is done with the diffrent libraries stored in *ffmpeg*. Be aware that converting the codec to AV1 can take a really long time as this codec is the most complete, most novel, and with higher quality, the other codecs should not take longer than 30s to convert a 720p video of 10 seconds in a standart meduim quality computer.
* **Compare the 4 codecs**: In the same file, we find a fucntions that will take four videos and gather them together in a 2x2 grid. The intention behind this fucntion is to compare the 4 diferent codecs. Thus, the first function should be executed for a same 4, convert the video to the 4 different codecs, and then join them inorder to compare the results. The functions read input form the user to select the 4 videos. The are no control, thus the size of the videos should be the same for an accuerate comparaison. In the video forlder, we provide a example of the results with a video of 10 seconds at 720p. (Comment on the results further down).
* **Stream a video**: The following operation find on the *stream_video.py* file, as the name describes, will stream a video to a given local network. The procedure is easy, the user must especify the video file, the network IP and the selected PORT. Once everything is introduced, the video can be open with *ffplay udp://IP:PORT* or using the VLC software and opening a local network retransmision, in this case we can directly especify udp://@:PORT. To stop the stream, introduce [q] on the execution terminal.


# Usage

The code works by reading user input to select the exercices and diferent opertions. Whenever a file is required, it must be intorduced with its format (.txt, .mp4, etc).
Then the other inputs required are explained in the output.
As required by the practice, everything is encapsuled in a class, even tho some operations are not logical, we have still created the class and put them there to show case we can work with classes. 


## Contact

Iker Diaz Cilleruelo - iker.diaz01@estudiant.upf.edu
Project Link: [https://github.com/IkerDC/SCAV-P2](https://github.com/IkerDC/SCAV-P2)

## Acknowledgements
* [FFmpeg](https://ffmpeg.org/)
* [FFmpeg Seeking](https://trac.ffmpeg.org/wiki/Seeking)
* [FFmpeg Audio](https://trac.ffmpeg.org/wiki/Encode/AAC)
* [Broacasting standarts](https://en.wikipedia.org/wiki/Broadcast_television_systems)
