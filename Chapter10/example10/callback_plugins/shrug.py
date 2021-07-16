from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    callback: shrug
    type: stdout
    short_description: modify Ansible screen output
    version_added: 4.0
    description:
        - This modifies the default output callback for ansible-playbook.
    extends_documentation_fragment:
      - default_callback
    requirements:
      - set as stdout in configuration
'''

from ansible.plugins.callback.default import CallbackModule as CallbackModule_default

class CallbackModule(CallbackModule_default):
  CALLBACK_VERSION = 2.0
  CALLBACK_TYPE = 'stdout'
  CALLBACK_NAME = 'shrug'

  def __init__(self):
    super(CallbackModule, self).__init__()

  def v2_playbook_on_stats(self, stats):
    msg = b'\xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf'
    self._display.display(msg.decode('utf-8') * 8)
    super(CallbackModule, self).v2_playbook_on_stats(stats)

