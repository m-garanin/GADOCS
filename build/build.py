#!/usr/bin/env python
import os
from time import time
from shutil import copyfile

from flask import Flask
from flask import render_template

import markdown2

from sections import G_POST_GROUP


G_PATH = "../CONTENT"
G_OUT = "../OUT"
G_POSTS = {} # {name: {'en': ('en-title', 'en-txt'), 'ru': ('ru-title','ru-txt'), ...} }

app = Flask(__name__)


def start():

    # STAGE 1 (prepare posts in memory)
    for root, dirs, files in os.walk(G_PATH):
        s1_convert_one_folder(root, files)

    # STAGE 2 (render to html)
    #print G_POSTS
    for pname, langs in G_POSTS.items():
        s2_render_page(pname, langs)
    
#--------------------------------------------------
#  STAGE 1
#--------------------------------------------------
def s1_convert_one_folder(root, files):
    en_md = os.path.join(root, 'en.md')
    if not os.path.exists(en_md):
        return

    path = root.split(os.sep)
    # path[2:]
    for fn in files:
        #print root, fn
        s1_convert_one_file(path[2:], fn)
        
           
def s1_convert_one_file(paths, fname):
    folder = os.path.join(G_OUT, paths[-1].lower())
    if not os.path.exists(folder):
        os.makedirs(folder)

    if fname.endswith(('jpeg', 'png', 'jpg')):
        return s1_convert_image(paths, fname)

    if fname.endswith(".md"):
        return s1_convert_md(paths, fname)
        
    #print folder, fname

    
def s1_convert_md(paths, fname):
    md_path = os.path.join(G_PATH, *paths) + "/" + fname

    post_name = paths[-1]
    lang = fname.replace(".md","")
    
    if fname == "en.md":
        lang_fname = "index.html"
    else:
        lang_fname = fname.replace(".md", ".html")
    
    md_text = open(md_path, 'rb').read().decode('utf-8')
    title = get_title(md_text)

    classes = {'img':'img-thumbnail rounded mx-auto mx-auto d-block'}
    kw = {'html-classes': classes}
    content = markdown2.markdown_path(md_path, extras=kw)
    
    add_post(post_name, lang, title, content)
    
    
def s1_convert_image(paths, fname):
    src = os.path.join(G_PATH, *paths) + "/" + fname
    dst = os.path.join(G_OUT, paths[-1].lower()) + "/" +  fname
    #print src, dst
    copyfile(src, dst)

    
def get_title(txt):
    "read title from text (as first line)"
    parts = txt.split("\n")
    title = ''
    for p in parts:
        if p:
            title = p
            break
    title = title.replace("**",'').replace("#", '').strip()
    return title


def add_post(pname, lan, title, html):
    """
    pname - post name (rtmp-example-post)
    lan - language code (en, ru, es)
    title - title by language
    html - html content
    """
    pname = pname.lower()
    p_inf = G_POSTS.get(pname, {})
    p_inf[lan] = (title, html)
    G_POSTS[pname] = p_inf


#--------------------------------------------------
#  STAGE 2
#--------------------------------------------------
def s2_render_page(pname, langs):
    for lng, (title, content) in langs.items():
        s2_render_lang(pname, lng, title, content)

        
def s2_render_lang(pname, lng, title, content):
    print lng, title, type(title)#, title.encode('unicode')

    def tr(post_name):
        """ return (title, url) for postname in lng
        url is '/post-name/index.html' or '/post-name/ru.html'
        """
        inf = G_POSTS[post_name]
        linfo = inf.get(lng, None)
        if not linfo:
            linfo = inf.get('en')
            url = '/%s/index.html' % post_name
        else:
            url = '/%s/%s.html' % (post_name, lng if lng !='en' else 'index')
        
        
        return (linfo[0], url, post_name==pname)
    
    
    if lng == "en":
        lang_fname = "index.html"
    else:
        lang_fname = lng + ".html"
    
    html_dst = os.path.join(G_OUT, pname) + "/" +  lang_fname

    group = G_POST_GROUP.get(pname,[])
    
    data = dict(title=title, content=content, group=group, tr=tr)
    html = render_page('post.html', data)
    
    #print html
    f = open(html_dst, "wb")
    f.write(html.encode('utf-8'))
    f.close()


    
    
def render_page(tmpl_name, pg):
    ctx = {'time': int(time())}
    
    for k,v in pg.items():
        ctx[k.upper()] = v
    
    html = render_template(tmpl_name, **ctx)
    
    return html


    
if __name__ == '__main__':
    with app.app_context():
        start()

