#!/usr/bin/env python
import os

G_PATH = "../CONTENT"
G_OUT = "../OUT"

def start():
    
    for root, dirs, files in os.walk(G_PATH):
        convert_one_folder(root, files)
        continue

    
def convert_one_folder(root, files):
    en_md = os.path.join(root, 'en.md')
    if not os.path.exists(en_md):
        return

    for fn in files:
        print root, fn
        #convert_one_file(root, fn)
        
            
def convert_one_file(paths, fname):
    folder = os.path.join(G_OUT, *paths)
    if not os.path.exists(folder):
        os.makedirs(folder)

    if fname.endswith(('jpeg', 'png', 'jpg')):
        return convert_image(paths, fname)
        
    print folder, fname

def convert_image(paths, fname):
    print "IMAGE:", fname
    

if __name__ == '__main__':
    #with app.app_context():
    start()

