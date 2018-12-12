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
def list2string(a):
    s = ''
    i = 0
    while i < len(a):
        if isinstance(a[i], str):
            s += a[i]
        elif isinstance(a[i], list):
            s += list2string(a[i])
            if i < len(a) - 1:
                s += '\n'
        else:
            s += str(a[i]) 
        i += 1
    return s

def replace(s, f, r, all=True):
    j = 0 #keyword check index
    out = ''
    for i in range(len(s)):
        if s[i] == f[j]:
            j += 1 #advance check index to check if next letter matches
            if len(f) == j: #the whole string found
                out += r #replace keyword with replacement
                if not all: #if we're only replacing the first occurence
                    return out + s[i+2:] #possible index error
                j = 0
        elif 0 < j: #if the word turns out not to be our keyword
            out += s[i-j: i] + s[i] #add all the charcters we missed
            j = 0 #reset the keyword check index
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

columnset = ''
for a in imgsets:
    columnset += replace(
        column,
        '&img',
        list2string(a),
        False)

html = replace(gallery, '&column', columnset, False)

with open('../'+article+'/gallery.html', 'w') as f:
    f.write(html)
