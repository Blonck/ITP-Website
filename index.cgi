#!/home/mueller/env/bin/python 
import wsgiref.handlers
from route import app

wsgiref.handlers.CGIHandler().run(app)
