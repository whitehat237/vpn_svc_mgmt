#!/usr/bin/python2

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook import Playbook
from ansible.executor.playbook_executor import PlaybookExecutor

Options = namedtuple('Options', ['connection',  'forks', 'become', 'become_method', 'become_user', 'check', 'listhosts', 'listtasks', 'listtags', 'syntax', 'module_path'])

variable_manager = VariableManager()
loader = DataLoader()
options = Options(connection='local', forks=100, become=true, become_method=sudo, become_user=None, check=False, listhosts=False, listtasks=False, listtags=False, syntax=False, module_path="")
passwords = dict(vault_pass='secret')

inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')
variable_manager.set_inventory(inventory)
playbooks = ["./vpn.yaml"]

executor = PlaybookExecutor(
              playbooks=playbooks,
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords)

executor.run()
