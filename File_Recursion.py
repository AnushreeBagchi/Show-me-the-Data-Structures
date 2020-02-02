import os

def find_files(suffix, path):
    return return_find_files(suffix, path, list())

def return_find_files(suffix, path, files):
    if os.path.isfile(path):
        if path.endswith(suffix):
            files.append(path)
    elif os.path.isdir(path):
        contents = os.listdir(path)
        for content in contents:
            new_path = os.path.join(path, content)
            return_find_files(suffix, new_path, files)
    return files

print("Pass" if (find_files(".c","./testdir") == ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']) else "Fail")
print("Pass" if find_files(".c","./testdir/t1.c") == ["./testdir/t1.c"] else "Fail") 
print("Pass" if find_files(".c","") == [] else "Fail") #edge case when path is not provided
print("Pass" if find_files(".c","./testdir/subdir") == [] else "Fail") #edge case when given path do not exist
print("Pass" if find_files(".c","./testdir/subdir2") == [] else "Fail") 
