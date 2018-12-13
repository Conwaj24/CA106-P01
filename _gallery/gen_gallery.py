#gallery generation script by Jordan
#note that this script is made with Python3, Python2 may cause errors

import os
from os import listdir
import sys

article = sys.argv[1]
columns = 4

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
    i = 0
    while i < x:
        out.append([])
        i += 1
    return out

def img_id(img):
    return 'lightbox-' + img.split('.')[0]

gallery = read_file('gallery.html')
column = read_file('column.html')
img = read_file('img.html')
lightbox = read_file('lightbox.html')
prev = read_file('prev.html')
next = read_file('next.html')

imgs = listdir('../'+article+'/img')

descs = {}
a = listdir('../'+article+'/desc')
for desc in a:
    key = desc.split('.')[0]
    val = read_file('../'+article+'/desc/'+desc)
    descs[key] = val

imgsets = empty_matrix(columns)
i = 0
while i < len(imgs):
    img_i = replace(img, '&src', 'img/'+imgs[i])
    img_i = replace(img_i, '&id', img_id(imgs[i]))
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

lightboxset = ''
for i in range(len(imgs)):
    lb = lightbox
    
    prv = prev if 0 < i else ''
    lb = replace(lb, '&prev', prv, False)

    nxt = next if i < len(imgs)-1 else ''
    lb = replace(lb, '&next', nxt, False)

    lb = replace(lb, '&id', img_id(imgs[i]))
    lb = replace(lb, '&indx', str(i+1), False)
    lb = replace(lb, '&len', str(len(imgs)), False)
    lb = replace(lb, '&src', 'img/'+imgs[i])

    key = imgs[i].split('.')[0]
    if key in descs:
        lb = replace(lb, '&desc', descs[key])
    else:
        lb = replace(lb, '&desc', '')

    lightboxset += lb

html = replace(html, '&lightbox', lightboxset, False)

with open('../'+article+'/gallery.html', 'w') as f:
    f.write(html)
