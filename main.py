__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile
import fileinput


def clean_cache():
    cwd = os.getcwd()
    dir_list = os.listdir(cwd)
    path = os.path.join(cwd, 'cache')
    if 'cache' not in dir_list:
        os.mkdir(path)
    elif 'cache' in dir_list:
        dir_cache = os.listdir(path)
        print(dir_cache)
        if len(dir_cache) > 0:
            for item in dir_cache:
                path_item = os.path.join(path, item)
                os.remove(path_item)
    print(dir_list)

# print(clean_cache())


def cache_zip(zip_file_path, cache_dir_path):
    zip = zipfile.ZipFile(zip_file_path)
    zip.extractall(cache_dir_path)

# cache_zip('data.zip', 'cache')


def cached_files():
    path = os.path.abspath('cache')
    return [entry.path for entry in os.scandir(path) if entry.is_file()]

# print(cached_files())


def find_password(cashed_files):
    for line in fileinput.input(cashed_files):
        if 'password' in line:
            print('Password found:', line)
            index = line.find(" ")
            password = line[index + 1: len(line) + 1]
            print(password)
    return password


find_password(cached_files())
