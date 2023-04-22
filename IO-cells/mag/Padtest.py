import subprocess
import numpy as np
import os
import glob
import os
import shutil
import readline

"""
This code receives as input a .mag file and generates a .spice file with extracted parasitances (R&C)
The tolerance for extracting R parasitances is 1e6 [see line 21 for whole commands]

"""

whole_file = ""


def extract(archivo):
    filename = archivo
    if filename.endswith(".mag"):
        filename = filename[:-4]

    useless_cat_call = subprocess.Popen(["magic", "-dnull", "-noconsole", archivo], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) # run file

    output, errors = useless_cat_call.communicate(
        input="extract do local\nextract all\n\next2sim labels on\next2sim\n\nextresist tolerance 1000000\nextresist\n\next2spice lvs\next2spice cthresh 0\next2spice extresist on\next2spice\n\nquit\n")
    useless_cat_call.wait()
    print(output)
    print(errors)


    # Set the file extensions and filenames to delete
    extensions_to_delete = [".ext"]
    files_to_delete = [filename+".nodes", filename+".sim"]

    # Delete files with the specified extensions
    for ext in extensions_to_delete:
        for file in os.listdir():
            if file.endswith(ext):
                os.remove(file)

    # Delete the specified files
    for file in files_to_delete:
        try:
            os.remove(file)
        except OSError:
            pass
    
    change_name_and_move()


    

def change_sigpad(archivo_pad):
    
    with open("Padtest.mag", "r") as file:
        lines = file.readlines() # saves all file lines as a list.
            
        for i, line in enumerate(lines):
            if ("use SigPad") in line:
                lines[i] = "use "+archivo_pad+"  "+archivo_pad+"_0\n"


    with open("Padtest.mag", "w") as file:
        file.writelines(lines) # write all list elements into the file.


def change_name_and_move():
    # specify the file name you want to rename
    old_file_name = 'Padtest.spice'

    # specify the new name for the file
    new_file_name = old_file_name.replace(".spice","")+whole_file.replace("SigPad","")+".spice"
    
    # get the current working directory
    cwd = os.getcwd()

    # join the current working directory and the old file name to create the old file path
    old_file_path = os.path.join(cwd, old_file_name)

    # join the current working directory and the new file name to create the new file path
    new_file_path = os.path.join(cwd, new_file_name)

    # use the os.rename() method to rename the file
    os.rename(old_file_path, new_file_path)

    source_path = './' + new_file_name
    # specify the destination directory path
    destination_path = '../ngspice/'

    # # use the shutil module's move() method to move the file
    shutil.move(source_path, destination_path)



def change_location():
    # specify the filename and the path of the file to be moved
    filename = 'Padtest.spice'



#-------------------------------
# set the tab key as the autocomplete key
readline.parse_and_bind('tab: complete')
whole_file = input("\nWrite pad test to be extracted [e.g SigPad_]: ")
whole_file = whole_file.replace(".mag","")
change_sigpad(whole_file)
extract("Padtest.mag")
