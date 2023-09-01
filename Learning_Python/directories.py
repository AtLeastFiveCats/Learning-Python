import os
import time

#C:\Users\Mrche\Desktop\Coding\Games
#chdir() changes the current directory
os.chdir("C:\\Users\Mrche\Desktop\Coding")
#getcwd() tells the current directory
print(os.getcwd())
#shows all files/directories in current directory
print(os.listdir())
#mkdir() makes a new directory in current directory if no path is specified
os.mkdir("test")
#rename renames a directory
os.rename("test", "new_test")

with open("newtext.txt", "w") as f:
    f.write("Text in the file!")

time.sleep(2)
#rmdir() removed a directory
os.rmdir("new_test")
#remove() removes a file
os.remove("newtext.txt")