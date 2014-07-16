#!/home/mueller/env/bin/python
# -*- coding: utf-8 -*-
import os
import glob
import time
from datetime import datetime
import jinja2 as j2
from flask.ext.misaka import markdown
from flask import Markup

blogposts = []
empty_post = {"text": "##Nothing\nHere\n", "cdate": datetime.utcnow(),
              "mdate": datetime.utcnow()}
blogposts.append(empty_post)

def make_blogposts():
    blogposts = []
    search_dir = "./blogposts/"
    files = filter(os.path.isfile, glob.glob(search_dir + "*.blog"))
    files.sort(key=lambda x: -1.0*os.path.getctime(x))
    for blogpost in files:
        with open(blogpost, "r") as myfile:
            data = Markup(markdown(myfile.read()))
            blogposts.append( {"text": data,
                               "mdate":datetime.utcfromtimestamp(os.path.getmtime(blogpost))})
    return blogposts
