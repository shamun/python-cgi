#!/usr/bin/python2.4
#
# Copyright - All Rights Reserved.
# 

"""
  Demo
  $ python /home/sun/Downloads/google_appengine/dev_appserver.py --host 0.0.0.0 /var/www/html/myrtc
"""
import cgi
import logging
import os
import random
import re
import json
import jinja2
import webapp2
import threading
from google.appengine.api import channel
from google.appengine.ext import db
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# Lock for syncing DB operation in concurrent requests handling.
# TODO(brave): keeping working on improving performance with thread syncing.
# One possible method for near future is to reduce the message caching.
LOCK = threading.RLock()

def generate_random(length):
  word = ''
  for _ in range(length):
    word += random.choice('0123456789')
  return word

class MainPage(webapp2.RequestHandler):
  def get(self):
    base_url = self.request.path_url
    user_agent = self.request.headers['User-Agent']
    pincode = self.request.get('pincode')
    template_values = {
      'pincode': pincode,
    }
    
    if pincode == '1234':
      template = jinja_environment.get_template('/html/index.html')
    else:
      template = jinja_environment.get_template('/html/index.html')    
    self.response.out.write(template.render(template_values))
    logging.info('User ')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    #('/message', ClassName1),
    #('/more/action/more/', ClassName2)
  ], debug=True)

