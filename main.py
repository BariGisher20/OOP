import os
from pprint import pprint

path = 'C:\\Users\\ПК\\Desktop\\Файл4'
res = os.listdir(path)


def lines_quantity(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        n = 0
        for line in file:
            n += 1
        return n


def create_dict(file_name):
    dict_line = []
    a = lines_quantity(file_name)
    dict_line.append(a)
    return sorted(dict_line)


def file_content(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()
        return content


def write(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for files in res[::-1]:
            if files.endswith(".txt"):
                keys = files
                values = lines_quantity(files)
                pprint(values)
                if values >0:
                    text = file_content(files)
                    res_3 = f'{keys}\n {values}\n {text}\n\n'

                    file.write(res_3)


pprint(write('new.txt'))
