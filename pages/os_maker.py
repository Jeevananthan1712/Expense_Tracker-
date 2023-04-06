import os
directory = "GeeksforGeeks"
parent_dir = r"C:\Users\JEEVA\Downloads"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)
newpath = r"C:\Users\JEEVA\Downloads\GeeksforGeeks"
# os.open(newpath)
os.access(newpath, os.F_OK)
new_parent_dir = r"C:\Users\JEEVA\Downloads\GeeksforGeeks"
new_directory = "NewFloder"
new_path = os.path.join(new_parent_dir, new_directory)
os.mkdir(new_path)
