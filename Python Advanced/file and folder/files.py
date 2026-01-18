import os
import shutil

print(os.listdir("."))
# print(os.rename("abc.py", 'xyz.py'))  # Renaming a file
# print(os.remove("xyz.py"))  # Deleting a file
# print(os.makedirs("hello")) # Creating a folder
# print(os.path.exists("hello")) # Checking if a folder exists

# print(shutil.copy("files.py", "./hello/"))
# print(shutil.move("./hello/files1.py", "./"))
print(shutil.rmtree("hello"))  # Deleting a folder and its contents