import os
from contextlib import contextmanager


# changing directory from one loc to another
# cwd = os.getcwd() #cwd - current working directory
# os.chdir('Sample-Dir-One')
# print(os.listdir())
# os.chdir(cwd)
#
# cwd = os.getcwd()
# os.chdir('Sample-Dir-Two')
# print(os.listdir())
# os.chdir(cwd)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())
