import os

base_dir = "./"

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

folders = ["day" + str(i) for i in range(1, 31)]
files = ["first.py", "second.py", "input.txt", "example1.txt", "example2.txt"]

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path)

for folder in folders:
    for file in files:
        file_path = os.path.join(base_dir, folder, file)
        
        if file.endswith(".py"):
            with open(file_path, 'w') as f:
                if file == "first.py":
                    with open("example1.py", 'r') as example_file:
                        f.write(example_file.read())
                elif file == "second.py":
                    with open("example2.py", 'r') as example_file:
                        f.write(example_file.read())
        elif file.endswith(".txt"):
            open(file_path, 'a').close()


print("Folders and files created successfully.")
