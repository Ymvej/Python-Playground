import os
cwd = os.getcwd()
writepath = cwd + '/fic.txt'
print(cwd)
print(writepath)
mode = 'a' if os.path.exists(writepath) else 'w'
with open(writepath, mode) as f:
    f.write('Hello, world!\n')