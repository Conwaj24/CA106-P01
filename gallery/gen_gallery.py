import os
from os import listdir
import sys

args = sys.argv[1:]
article = args[0]
columns = args[1]

def read_file(s):
    out = ''
    with open(s) as f:
        out = f.read()
    return out

gallery = read_file('gallery.html')
column = read_file('column.html')
img = read_file('img.html')

print (listdir('../'+article+'/img'))
