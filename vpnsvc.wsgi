#!/usr/bin/python

import cStringIO
import subprocess
output = ''

def application(environ, start_response):
    headers = []
    headers.append(('Content-Type', 'text/html'))
    write = start_response('200 OK', headers)

    input = environ['wsgi.input']
    output = cStringIO.StringIO()

    method = environ['REQUEST_METHOD']
    if method != 'GET':
        #output 'Invalid Request Method'
        return ['400 Bad Request']
 

    query = environ['QUERY_STRING']
    #print >> output, query +'<BR>'
    
    mylist = query.split('=')


    if 'service' in mylist[0]:
        state = mylist[1]

        if state == 'start' or 'stop':

            playbook = '/usr/local/ansible/' + state + '-vpn.yaml'
            p = subprocess.Popen(['/bin/sudo', '/bin/ansible-playbook', playbook], stdout=subprocess.PIPE)
            out = p.communicate()
            print >> output, out 
            output.write(input.read(int(environ.get('CONTENT_LENGTH', '0'))))
            return [output.getvalue()]    

        else:
            return ['Invalid Request']
