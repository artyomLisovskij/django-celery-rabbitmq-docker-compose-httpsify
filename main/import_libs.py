import os
import stat
import json
import re
import random, string
import datetime

from .models import *
from .forms import *

from django import forms

from urllib.parse import unquote
from tempfile import NamedTemporaryFile

from celery.result import AsyncResult
from django.conf import settings
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.utils.encoding import smart_str
from django.views.decorators.http import require_POST

from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import force_bytes
from django.core import serializers




import datetime
from datetime import date, time, timedelta


''' redis time '''
import redis

POOL = redis.ConnectionPool(host='redis', port=6379, db=0)

def getVariable(variable_name):
    my_server = redis.Redis(connection_pool=POOL)
    response = my_server.get(variable_name)
    return response

def setVariable(variable_name, variable_value):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.set(variable_name, variable_value)
# redis.incr('hits')
# redis.get('hits')



from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging
import logging


# TODO: SENTRY data
#handler = SentryHandler('')
#setup_logging(handler)

#logger = logging.getLogger(__name__)