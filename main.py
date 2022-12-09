import pathlib
import shutil
import os
import re

class ANSI():
    def color(bg, fg, style):
        return "\33[{bg};{fg};{style}m".format(bg=bg, fg=fg, style=style)


all_ext = open("ext-to-filter.txt", "r").read().split("\n")
if "" in all_ext:
    all_ext.remove("")
print("Filtering by : " + str(all_ext))

nbfiles = 0
file_nb = 1
file_moved = 0

for path in pathlib.Path("./input").iterdir():
    if path.is_file():
        nbfiles += 1
print("There is " + str(nbfiles) + " files in the input folder.")

for path in pathlib.Path("./input").iterdir():
    file = pathlib.PurePosixPath(path).name
    
    for ext in all_ext:
        if file.endswith(ext):
            print("--> " + ANSI.color(7, 49, 32) + "File \"" + str(file) + "\" (file number " + str(file_nb) + ") is a " + str(ext) + " file" + ANSI.color(0, 94, 39))
            file_moved += 1
            
            if os.path.exists("./output/" + str(ext)) == False:
                os.mkdir("./output/" + str(ext))
            
            output_folder = "./output/" + str(ext) + "/"
            shutil.move("./input/" + str(file), str(output_folder) + str(file))
            
            break
        elif file == "the-folder-where-you-put-files":
            break
        else:
            print("    File \"" + str(file) + "\" (file number " + str(file_nb) + ") is not a " + str(ext) + " file")
    print("\n")
    file_nb += 1

print("Successfully moved " + str(file_moved) + " files out of " + str(nbfiles) + " files in the output folder !")
exit = input("Press enter to exit: ")