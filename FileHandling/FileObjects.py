# Read and write file

f = open("testDemo.txt", "r")
f_context = f.read()
print(f.name)
# print(f_context)
# print(f.mode) tells the mode whether it is read or write 'r' or 'w'
f.close()

# Context manager
with open("testDemo.txt") as f:
    size = 10
    read = f.read(size)
    # readline = f.readline()  # reads single line
    # readCharac = f.read(10)  # reads 10 characters
    # print(readline)
    # print(readCharac)

    # using for loop
    # for line in f:
    #     print(line, end="")

    # using while loop
    while len(read) > 0:
        print(read, end="")
        read = f.read(size)

with open("testWrite.txt", 'w') as w:
    w.write("Test")
    w.write("Test")
    w.write("Test")
    w.seek(0)
    w.write("OR")

# read and write from one file to another file
with open("testDemo.txt", 'r') as rf:
    with open("testWrite2.txt", 'w') as wf:
        for line in rf:
            wf.write(line)

# dealing with images
with open("testImage.png", 'rb') as ri:
    with open("testImage_copy.png", 'wb') as wi:  # here wb refers to binary mode
        for img in ri:
            wi.write(img)

# Copying the image with chunks:
# with open("testImage.png", "rb") as rf:
#     with open("testImage_copy.png", "wb") as wf:
#         chunk_size = 4096
#     rf_chunk = rf.read(chunk_size)
#     while len(rf_chunk) > 0:
#         wf.write(rf_chunk)
#         rf_chunk = rf.read(chunk_size)
