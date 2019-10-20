import glob

import json 

path = './*.md'
files=glob.glob(path)
md_files1 = []
for file in files:
    f=open(file, 'r')
    content=f.read()
    hashtag = content.splitlines()[0]
    tip = content.splitlines()[1:]
    md_files = {'hashtag':hashtag, 'tip':tip}
    md_files1.append(md_files)
print(md_files1)
