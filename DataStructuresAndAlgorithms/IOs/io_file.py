#   modes
#   'r'       open for reading (default)
#   'w'       open for writing, truncating the file first
#   'x'       create a new file and open it for writing
#   'a'       open for writing, appending to the end of the file if it exists
#   'b'       binary mode
#   't'       text mode (default)
#   '+'       open a disk file for updating (reading and writing)
#   'U'       universal newline mode (deprecated)

f = open("test.txt")

# this will take care of opening and closing the file handle
with open("test.txt", 'w', encoding="utf-8") as f:
    f.write("This is the first\n")
    f.write("This is the second line\n")
    f.write("This is the third line\n")
    f.write("This is the fourth line")


with open("test.txt", 'a', encoding="utf-8") as f:
    f.write("Appending more lines of code\n")
    f.write("Appending more lines of code ..\n")
    f.write("Appending more lines of code ...\n")

with open("test.txt", 'r', encoding="utf-8") as f:
    print(f.read())


# seek it to the first character
# myFile.seek(0)

