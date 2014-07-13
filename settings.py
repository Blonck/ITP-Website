#!/home/mueller/env/bin/python
# -*- coding: utf-8 -*-

login = "marenz"

# define who you are:
# TODO: why is utf-8 not working?
name = u"Martin Marenz"  # why is utf-8 not working?
room = "116"
email = "martin.marenz@itp.uni-leipzig.de"
phone = "+49 (0)341 97 32466"
# path to the picture that appears at the about page
photo = "static/blank.jpg"

# define the root of your www - path in the filesystem
root = "/home/" + login + "/www/"
# define the root of the web path
# IMPORTANT: make sure this ends with a slash!
base = "https://www.physik.uni-leipzig.de/~" + login + "/index.cgi/"

# title of the page
title = u"{0}".format(name)

# defines how links are called in the navigation bar
# every line is a tuple of ( caption, filename ), where '.html'
# is appended automatically from the framework
# - links appear in the same order they are defined here
# IMPORTANT:
# I don't fully understand our server configuration. It turned out that naming
# a link 'index' or 'publications' did not work
navigation = [
    ('About', 'about'),
    ('Publication', 'published'), # don't name this publications -- gets you back to the itp...
    ('Personal', 'personal'),
    ('Vim', 'vim'),
    ]
