#  file operation examples
import os

print(os.getcwd())

print(os.listdir("/Users/kumaransugumar"))

# shutil.move("practice.txt", "/Users/kumaransugumar/pythonPyCharm")

#  send2trash.send2trash("practice.txt")
#  this is not working need to check later

f = open("practice.txt", "+w")
f.write("This is for testing and nothing else")
f.close()

for folder, subfolders, files in os.walk("/Users/kumaransugumar/"):

    print(f"Currently looking at {folder}")

    for sub_fold in subfolders:
        print(f" SubFolder {sub_fold}")
