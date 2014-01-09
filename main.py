import os
import webapp2
import jinja2

from google.appengine.ext import db
from time import sleep

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **lw):
        self.response.out.write(*a, **lw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Posti(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)


class NewPostPage(Handler):
    def render_front(self, subject="", content="", error=""):
        self.render("front.html", subject=subject, content=content, error=error)

    def render_perma(self, subject="", content="", link=""):
        self.redirect("/?link=" + link)

    def get(self):
        self.render_front()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if subject and content:
            a = Posti(subject = subject, content = content)
            a.put()
            link = str(a.key().id())
            sleep(1)
            self.render_perma(subject=subject, content=content, link=link)
        else:
            error = "we need both a subject and some content!"
            self.render_front(subject=subject, content=content, error=error)

class MainHandler(Handler):
    def render_front(self, subject="", content="", error=""):
        postis = db.GqlQuery("SELECT * FROM Posti ORDER BY created DESC")
        self.render("mainpage.html", postis=postis)

    def get(self):
        self.render_front()

class PermaLink(Handler):
    def render_front(self, link=""):
        Posti.get_by_id(link)
        self.render("perma.html")


app = webapp2.WSGIApplication([('/', MainHandler), ('/newpost', NewPostPage), (r'/(\d+)', PermaLink)], debug=True)
