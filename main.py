import os
import convert_codec as vc



def switch(exercice):
    if (exercice == "1"):
        print("Filename:")
        file = input()
        print("Introduce format from \"vp8\",\"vp9\",\"h265\" or \"av1\"")
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
        os.system("ffplay codec_compaire.mp4")
        return True
    else:
        return False

switch("3")