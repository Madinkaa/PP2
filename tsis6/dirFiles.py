#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def list(path):
    dir_path = os.path.dirname(path)
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            print("File:", item)


path = "C:\\Users\\madina.myrzakhan\\Desktop"
list(path)

#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os

def check_path_access(path):
   
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    
    if not os.access(path, os.R_OK):
        print("Path is not readable.")
    else:
        print("Path is readable.")

    
    if not os.access(path, os.W_OK):
        print("Path is not writable.")
    else:
        print("Path is writable.")

    
    if not os.access(path, os.X_OK):
        print("Path is not executable.")
    else:
        print("Path is executable.")


path = "C:\\Users\\madina.myrzakhan\\Desktop"
check_path_access(path)


#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

def test_path(path):
    if os.path.exists(path):
        print("Path exists.")

        filename = os.path.basename(path)
        print("Filename:", filename)

        directory = os.path.dirname(path)
        print("Directory:", directory)
    else:
        print("Path does not exist.")

path = "C:\\Users\\madina.myrzakhan\\Desktop"
test_path(path)

#Write a Python program to count the number of lines in a text file.
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
            print("Number of lines:", line_count)
    except FileNotFoundError:
        print("File not found.")

file_path = "C:\\Users\\madina.myrzakhan\\Desktop\\number.txt"
count_lines(file_path)

#Write a Python program to write a list to a file.
def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print("List has been written to the file.")
    except IOError:
        print("An error occurred while writing to the file.")

file_path = "C:\\Users\\madina.myrzakhan\\Desktop\\number.txt"
data_list = [1, 2, 3, 4, 5]
write_list_to_file(file_path, data_list)

#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string

def generate_files():
    for letter in string.ascii_uppercase:
        file_name = letter + ".txt"
        with open(file_name, 'w') as file:
            file.write("This is file {}.".format(file_name))
        print("File {} created.".format(file_name))

generate_files()

#Write a Python program to copy the contents of a file to another file
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File contents copied successfully.")
    except IOError:
        print("An error occurred while copying the file.")

source_file = "path/to/source.txt"
destination_file = "path/to/destination.txt"
copy_file(source_file, destination_file)

#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

def delete_file(path):
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    if not os.path.isfile(path):
        print("Path is not a file.")
        return

    if not os.access(path, os.W_OK):
        print("File is not accessible for deletion.")
        return

    try:
        os.remove(path)
        print("File deleted successfully.")
    except OSError:
        print("An error occurred while deleting the file.")

file_path = "C:\\Users\\madina.myrzakhan\\Desktop\\number.txt"
delete_file(file_path)

