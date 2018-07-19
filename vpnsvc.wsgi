#!/usr/bin/python

import cStringIO
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager


def application(environ, start_response):
    headers = []
    headers.append(('Content-Type', 'text/plain'))
    write = start_response('200 OK', headers)

    input = environ['wsgi.input']
    output = cStringIO.StringIO()

    keys = environ.keys()
    keys.sort()


    method = environ['REQUEST_METHOD']
    if method != 'GET':
        #output 'Invalid Request Method'
        return ['400 Bad Request']
 

    try:
        query = environ['QUERY_STRING'].split('service=')
        state = query[1] 
        print >> output, state

    except:
        print >> output, 'Invalid Parameter!  USAGE: ?service={start|stop|restart}'

    if state == 'start' or 'stop' or 'restart':
        run_vpn_playbook(state)


    print >> output
    output.write(input.read(int(environ.get('CONTENT_LENGTH', '0'))))
    return [output.getvalue()]    

def run_vpn_playbook(state):
    print >> output
    output.write(input.read(int(environ.get('CONTENT_LENGTH', '0'))))
    return [output.getvalue()]    
