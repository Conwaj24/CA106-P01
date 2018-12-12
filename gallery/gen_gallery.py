import os
from os import listdir
import sys

args = sys.argv[1:]
article = args[0]
columns = int(args[1])

def read_file(s):
    out = ''
    with open(s) as f:
        out = f.read()
    return out

def replace(s, f, r, all=True):
    j = 0
    out = ''
    for i in range(len(s)):
        if s[i] == f[j]:
            j += 1
            if len(f) == j: #the whole string found
                out += r
                if not all:
                    return out + s[i+2:] #possible index error
                j = 0
        elif 0 < j: 
            out += s[i-j: i] + s[i]
            j = 0
        else:
            out += s[i]
    return out

def empty_matrix(x=0, y=0):
    out = []
    for i in range(x):
        out.append([])
    return out

gallery = read_file('gallery.html')
column = read_file('column.html')
img = read_file('img.html')
imgs = listdir('../'+article+'/img')

imgsets = empty_matrix(columns)
imgsets[0].append(imgs[0])
i = 1
while i < len(imgs):
    img_i = replace(img, '&src', imgs[i])
    imgsets[i % columns].append(img_i)
    i += 1
print (imgsets)


