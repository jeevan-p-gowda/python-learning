import os
from dotenv import load_dotenv

# Enables user to perform Operating System (OS) functionality like mkdir, chdir (CRUD) etc

# prints all the methods in os module
print(dir(os))
# getcwd() - gets the current working directory
print(os.getcwd())

# chdir('Path') - changes the working directory
# os.chdir('/PythonLearning/')
print(os.getcwd())

# mkdir - creates directory
os.mkdir('OS_demo')

# rmdir - remove directory
os.rmdir('OS_demo')

# makedirs - creates multiple directory
os.makedirs('OS_demo2/sub-dir')

# removedir - remove directory
os.removedirs('OS_demo2/sub-dir')

# rename() - renames the file

# stat() - gives all the methods that fetches info of the file
# print(os.stat('PythonLearning/misc'))
# print(os.stat('/PythonLearning/misc').st_atime)

# walk - walksthrough the dir and files in it
# for dirpath, dirnames, filenames in os.walk('give path here'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('files:', filenames)
#     print()

# environ() - prints all the environ related info
print(os.environ.get('HOME'))
# path() - path related info
print(os.path.join(os.environ.get('HOME'), 'test.txt'))
print(os.path.exists(os.path.join(os.environ.get('HOME'), 'test.txt')))
print(os.path.isfile(os.path.join(os.environ.get('HOME'), 'test.txt')))
print(os.path.isdir(os.environ.get('HOME')))
print(os.path.basename(os.path.join(os.environ.get('HOME'), 'test.txt')))
print(dir(os.path))  # gives all functions of os.path

# system() - executes shell commands
os.system('ls')

# this method will be useful while maintaining secrets
# load_dotenv(dotenv_path='***/PythonLearning/misc/.env')
# print(os.getenv('JEEVAN'))
