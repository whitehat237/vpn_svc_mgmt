#import cStringIO
import os
from subprocess import call

def application(environ, start_response):
   headers = []
    headers.append(('Content-Type', 'text/plain'))
    write = start_response('200 OK', headers)

    #input = environ['wsgi.input']
    #output = cStringIO.StringIO()

    keys = environ.keys()
    keys.sort()

    for key in keys:
        if "QUERY_STRING" in key:
            if '=' in repr(environ[key]:
                query_value = repr(environ[key]).split('=')

                if "service" in query_value[0]:
                    state = query_value[1]

                    if state == 'start' or 'stop' or 'restart':
                        call(["sudo ansible-playbook ntp.yaml --extra-vars "svcstate=%s" % (state)]) 

    return [output.getvalue()]
