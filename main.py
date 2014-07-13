import flask, flask.views
import os
import settings

class Main(flask.views.MethodView):
    def get(self, page='about'):
        # TODO: read the documentation: is 'page' a secured filename already?
        pagehtml = page + ".html"
        if os.path.isfile('templates/' + pagehtml):
            return flask.render_template(pagehtml, settings=settings, current=page)
        else:
            flask.abort(404)
