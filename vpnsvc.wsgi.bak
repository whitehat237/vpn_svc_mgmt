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

    Options = namedtuple('Options', ['connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])

    # initialize needed objects
    variable_manager = VariableManager()
    loader = DataLoader()
    options = Options(connection='local', module_path='/path/to/mymodules', forks=100, remote_user=None, private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=None, become_method=None, become_user=None, verbosity=None, check=False)
    passwords = dict(vault_pass='secret')

    # create inventory and pass to var manager
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')
    variable_manager.set_inventory(inventory)

    # create play with tasks
    play_source =  dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [ dict(action=dict(module='debug', args=(msg='Hello Galaxy!'))) ]
    )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # actually run it
    tqm = None
    try:
        tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
              stdout_callback='default',
          )
    result = tqm.run(play)

    finally:
        if tqm is not None:
            tqm.cleanup()

    print >> output
    output.write(input.read(int(environ.get('CONTENT_LENGTH', '0'))))
    return [output.getvalue()]    
