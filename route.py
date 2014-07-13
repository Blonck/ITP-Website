#!/home/mueller/env/bin/python
# -*- coding: utf-8 -*-
import flask
import settings
from flask import render_template
from flask.ext.misaka import Misaka

# renders default content pages
from main import Main

app = flask.Flask(__name__)
Misaka(app)
app.application_root = settings.root

# Routing
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=['GET'])

app.add_url_rule('/<page>/',
                 view_func=Main.as_view('page'),
                 methods=['GET'])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', settings=settings), 404


if __name__ == "__main__":
    app.run(debug=True)
