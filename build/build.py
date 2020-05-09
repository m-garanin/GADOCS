#!/usr/bin/env python
import os
from shutil import copyfile

import markdown2

G_PATH = "../CONTENT"
G_OUT = "../OUT"

def start():
    
    for root, dirs, files in os.walk(G_PATH):
        convert_one_folder(root, files)
        

    
def convert_one_folder(root, files):
    en_md = os.path.join(root, 'en.md')
    if not os.path.exists(en_md):
        return

    path = root.split(os.sep)
    # path[2:]
    for fn in files:
        #print root, fn
        convert_one_file(path[2:], fn)
        
           
def convert_one_file(paths, fname):
    folder = os.path.join(G_OUT, *paths)
    if not os.path.exists(folder):
        os.makedirs(folder)

    if fname.endswith(('jpeg', 'png', 'jpg')):
        return convert_image(paths, fname)

    if fname.endswith(".md"):
        return convert_md(paths, fname)
        
    #print folder, fname

    
def convert_md(paths, fname):
    md_path = os.path.join(G_PATH, *paths) + "/" + fname

    if fname == "en.md":
        lang_fname = "index.html"
    else:
        lang_fname = fname.replace(".md", ".html")
    
    html_dst = os.path.join(G_OUT, *paths) + "/" +  lang_fname
    
    html = markdown2.markdown_path(md_path)
    #print html
    f = open(html_dst, "wb")
    f.write(html.encode('utf-8'))
    f.close()
    
    

def convert_image(paths, fname):
    src = os.path.join(G_PATH, *paths) + "/" + fname
    dst = os.path.join(G_OUT, *paths) + "/" +  fname
    #print src, dst
    copyfile(src, dst)

if __name__ == '__main__':
    #with app.app_context():
    start()
