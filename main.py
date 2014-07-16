import flask
import flask.views
import os
import settings
import blog
from datetime import datetime


class Main(flask.views.MethodView):
    def get(self, page='about'):
        # TODO: read the documentation: is 'page' a secured filename already?
        pagehtml = page + ".html"
        if page == "blog":
            if os.path.isfile('templates/' + pagehtml):
                blogposts = blog.make_blogposts()
                return flask.render_template(pagehtml, settings=settings,
                                             current=page,
                                             blogposts=blogposts,
                                             current_time=datetime.utcnow())
        if os.path.isfile('templates/' + pagehtml):
            return flask.render_template(pagehtml, settings=settings,
                                         current=page,
                                         current_time=datetime.utcnow())
        else:
            flask.abort(404)
