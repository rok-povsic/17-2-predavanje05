#!/usr/bin/env python
import webapp2

from handlers.base import MainHandler, CookieAlertHandler
from handlers.topics import TopicAddHandler, TopicShowHandler
from handlers.comments import CommentAddHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="cookie-alert-page"),
    webapp2.Route('/topic/add', TopicAddHandler),
    webapp2.Route('/topic/show/<topic_id:\d+>', TopicShowHandler),
    webapp2.Route('/topic/show/<topic_id:\d+>/comment/add', CommentAddHandler),
], debug=True)
