from contextlib import contextmanager


class Open_File:
    def __init__(self, fileName, mode):
        self.fileName = fileName
        self.mode = mode

    def __enter__(self, file):
        self.file = open(self.fileName, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Open_File("cmDemo.txt", 'w') as wf:
    wf.write("Hi Hevo")

print(wf.closed)


# using @contextmanager
@contextmanager
def open_file(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()


with open_file("cmDemo2.txt", 'w') as f:
    f.write("Hi hello world")

print(f.closed)
